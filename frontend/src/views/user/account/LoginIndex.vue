<template>
    <div class="flex justify-center mt-20">
        <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
            <label class="label">Username</label>
            <input type="text" class="input" placeholder="Username" />

            <label class="label">Password</label>
            <input type="password" class="input" placeholder="Password" />

            <button class="btn btn-neutral mt-4">Login</button>
            <RouterLink :to="{name: 'user-account-register-index'}" class="btn btn-ghost">Register</RouterLink>
        </fieldset>
    </div>
</template>

<script setup>
</script>

<style scoped>
</style>