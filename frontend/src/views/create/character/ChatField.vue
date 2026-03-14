<template>
    <dialog ref="modal-ref" class="modal">
        <div class="modal-box w-110 h-170" :style="modalStyle">
            <button @click="modalRef.close()" class="btn btn-sm btn-circle btn-ghost bg-transparent absolute right-1 top-1">✕</button>
                <InputField />
            <CharacterPhotoField v-if="friend" :character="friend.character" />
        </div>
    </dialog>
</template>

<script setup>
import {computed, useTemplateRef} from "vue";
import InputField from "./components/chat_field/InputField.vue";
import CharacterPhotoField from "./components/chat_field/CharacterPhotoField.vue";

const props = defineProps(['friend'])
const modalRef = useTemplateRef('modal-ref')

function showModal() {
    modalRef.value.showModal()
}

const modalStyle = computed(() => {
    if (props.friend) {
        return {
            backgroundImage: `url(${props.friend.character.background_image})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
        }
    } else {
        return {}
    }
})

defineExpose({ showModal })
</script>

<style scoped>

</style>
