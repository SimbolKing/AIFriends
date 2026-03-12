<template>
    <fieldset class="fieldset">
        <label class="label text-base">Username</label>
        <input v-model="myUsername" type="text" class="input w-108">
    </fieldset>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps(['username'])
const myUsername = ref(props.username)

watch(() => props.username, newVal => {
    myUsername.value = newVal
})

defineExpose({
    myUsername,
})
</script>

<style scoped>

</style>
