<script setup>
import Photo from '@/components/user/profile/Photo.vue';
import Profile from '@/components/user/profile/Profile.vue';
import Username from '@/components/user/profile/Username.vue';
import api from '@/js/http/api';
import { base64ToFile } from '@/js/utils/base64_to_file';
import { useUserStore } from '@/stores/user';
import { ref, useTemplateRef } from 'vue';

const user = useUserStore()

const photoRef = useTemplateRef('photo-ref')
const usernameRef = useTemplateRef('username-ref')
const profileRef = useTemplateRef('profile-ref')

const errorMessage = ref('')

async function handleUpdate() {
    const photo = photoRef.value.myPhoto
    const username = usernameRef.value.myUsername.trim()
    const profile = profileRef.value.myProfile.trim()

    errorMessage.value = ''

    if (!photo) {
        errorMessage.value = 'photo can not be empty'
    } else if (!username) {
        errorMessage.value = 'username can not be empty'
    } else if (!profile) {
        errorMessage.value = 'profile can not be empty'
    } else {
        const formData = new FormData()
        formData.append('username', username)
        formData.append('profile', profile)
        if (photo !== user.photo) {
            formData.append('photo', base64ToFile(photo, 'photo.png'))
        }
        try {
            const res = await api.post('/api/user/profile/update/', formData)
            const data = res.data
            if (data.result === 'success') {
                user.setUserInfo(data)
            } else {
                errorMessage.value = data.result
            }
        } catch (err) {
            console.log(err);
        }
    }
}
</script>

<template>
    <div class="flex justify-center">
        <div class="card bg-base-200 shadow-sm w-120 mt-20">
            <div class="card-body">
                <h3 class="text-lg font-bold my-2">Edit your profile</h3>
                <Photo ref="photo-ref" :photo="user.photo" />
                <Username ref="username-ref" :username="user.username" />
                <Profile ref="profile-ref" :profile="user.profile" />
                <p v-if="errorMessage" class="text-sm text-red-500">{{ errorMessage }}</p>
                <div class="flex justify-center">
                    <button @click="handleUpdate" class="btn btn-primary w-50 mt-2">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>