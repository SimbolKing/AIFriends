<script setup>
import { nextTick, onBeforeUnmount, ref, useTemplateRef, watch } from 'vue';
import CameraIcon from './icons/CameraIcon.vue';
import Croppie from 'croppie';
import 'croppie/croppie.css'

const fileInputRef = useTemplateRef('file-input-ref')
const modalRef = useTemplateRef('modal-ref')
const croppieRef = useTemplateRef('croppie-ref')

const props = defineProps(['photo'])
const myPhoto = ref(props.photo)
let croppie = null

watch(() => props.photo, newVal => {
    myPhoto.value = newVal
})

function onFileChange(e) {
    const file = e.target.files[0]
    e.target.value = ''
    if (!file) return

    const reader = new FileReader()
    reader.onload = () => {
        openModal(reader.result)
    }

    reader.readAsDataURL(file)
}

async function openModal(photo) {
    modalRef.value.showModal()
    await nextTick()

    if (!croppie) {
        croppie = new Croppie(croppieRef.value, {
            viewport: {width: 200, height: 200, type: 'square'},
            boundary: {width: 300, height: 300},
            enableOrientation: true,
            enforceBoundary: true,
        })
    }

    croppie.bind({
        url: photo,
    })
}

async function crop() {
    if (!croppie) return

    myPhoto.value = await croppie.result({
        type: 'base64',
        size: 'viewport',
    })

    modalRef.value.close()
}

onBeforeUnmount(() => {
    croppie?.destroy()
})

defineExpose({ myPhoto })
</script>

<template>
    <div class="flex justify-center">
        <div class="avatar relative">
            <div class="w-25 rounded-full">
                <img :src="myPhoto" alt="">
            </div>
            <div @click="fileInputRef.click()" class="absolute left-0 top-0 w-25 h-25 flex justify-center items-center bg-black/20 rounded-full cursor-pointer">
                <CameraIcon />
            </div>
        </div>
    </div>

    <input ref="file-input-ref" type="file" accept="image/*" class="hidden" @change="onFileChange">

    <dialog class="modal" ref="modal-ref">
        <div class="modal-box transition-none">
            <button @click="modalRef.close()" class="btn btn-circle btn-sm btn-ghost absolute right-2 top-2">
                ✕
            </button>
            <div ref="croppie-ref" class="flex flex-col justify-center my-4"></div>
            <div class="modal-action">
                <button @click="modalRef.close()" class="btn">Cancel</button>
                <button @click="crop" class="btn btn-neutral">Select</button>
            </div>
        </div>
    </dialog>
</template>

<style scoped>
</style>