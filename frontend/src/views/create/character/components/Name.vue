<template>
    <fieldset class="fieldset">
        <label class="label text-base">Character's name</label>
        <input v-model="myName" type="text" class="input w-108">
    </fieldset>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps(['name'])
const myName = ref(props.name)

watch(() => props.name, newVal => {
    myName.value = newVal
})

defineExpose({ myName })
</script>

<style scoped>

</style>
