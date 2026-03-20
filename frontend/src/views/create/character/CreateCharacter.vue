<template>
    <div class="flex justify-center">
        <div class="card w-120 bg-base-200 shadow-sm mt-5">
        <div class="card-body">
            <h3 class="text-lg font-bold">Create your AI character</h3>
            <Photo ref="photo-ref" />
            <Name ref="name-ref" />
            <Voice ref="voice-ref" :voices="voices" :curVoiceId="curVoiceId" />
            <Profile ref="profile-ref" />
            <BackgroundImage ref="background-image-ref" />

            <p v-if="errorMessage" class="text-sm text-red-500">{{ errorMessage }}</p>

            <div class="flex justify-center">
            <button @click="handleCreate" class="btn btn-neutral w-60 mt-2">Create</button>
            </div>
        </div>
        </div>
    </div>
</template>

<script setup>
import Photo from "./components/Photo.vue";
import Name from "./components/Name.vue";
import Profile from "./components/Profile.vue";
import BackgroundImage from "./components/BackgroundImage.vue";
import { ref, useTemplateRef, onMounted } from "vue";
import { base64ToFile } from "@/utils/base_64_to_file";
import api from "@/utils/http/api";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user.js";
import Voice from "./components/Voice.vue";

const user = useUserStore()
const router = useRouter()

const photoRef = useTemplateRef('photo-ref')
const nameRef = useTemplateRef('name-ref')
const voiceRef = useTemplateRef('voice-ref')
const profileRef = useTemplateRef('profile-ref')
const backgroundImageRef = useTemplateRef('background-image-ref')
const errorMessage = ref('')

const voices = ref([])
const curVoiceId = ref(null)

onMounted(async () => {
    try {
        const res = await api.get('/api/create/character/voice/get_list/', {})
        const data = res.data
        if (data.result === 'success') {
            voices.value = data.voices
            curVoiceId.value = data.voices[0].id
        }
    } catch (err) {
        console.error(err)
    }
})

async function handleCreate() {
    const photo = photoRef.value.myPhoto
    const name = nameRef.value.myName?.trim()
    const voice = voiceRef.value.myVoice
    const profile = profileRef.value.myProfile?.trim()
    const backgroundImage = backgroundImageRef.value.myBackgroundImage

    errorMessage.value = ''
    if (!photo) {
        errorMessage.value = "character's photo can not be empty"
    } else if (!name) {
        errorMessage.value = "character's name can not be empty"
    } else if (!voice) {
        errorMessage.value = 'Voice style can not be empty'
    } else if (!profile) {
        errorMessage.value = "character's profile can not be empty"
    } else if (!backgroundImage) {
        errorMessage.value = 'chat background can not be empty'
    } else {
        const formData = new FormData()
        formData.append('name', name)
        formData.append('voice_id', voice)
        formData.append('profile', profile)
        formData.append('photo', base64ToFile(photo, 'photo.png'))
        formData.append('background_image', base64ToFile(backgroundImage, 'background_image.png'))

        try {
        const res = await api.post('/api/create/character/create/', formData)
        const data = res.data
        if (data.result === 'success') {
            await router.push({
                name: 'user-space-index',
                params: {
                    user_id: user.id,
                }
            })
        } else {
            errorMessage.value = data.result
        }
        } catch (err) {
        }
    }
}
</script>

<style scoped>

</style>
