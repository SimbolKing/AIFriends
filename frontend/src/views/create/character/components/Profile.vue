<template>
    <fieldset class="fieldset">
        <label class="label text-base">Character's profile</label>
        <textarea v-model="myProfile" rows="3" class="textarea w-108"></textarea>
    </fieldset>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps(['profile'])
const myProfile = ref(props.profile)

watch(() => props.profile, newVal => {
    myProfile.value = newVal
})

defineExpose({ myProfile })
</script>

<style scoped>

</style>
