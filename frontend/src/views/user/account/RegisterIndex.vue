<template>
    <div class="flex justify-center mt-20">
        <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
            <label class="label">Username</label>
            <input type="text" class="input" placeholder="Username" />

            <label class="label">Password</label>
            <input type="password" class="input" placeholder="Password" />

            <label class="label">Confirm your password</label>
            <input type="password" class="input" placeholder="Confirm your password" />

            <button class="btn btn-neutral mt-4">Register</button>
            <RouterLink :to="{name: 'user-account-login-index'}" class="btn btn-ghost">Login</RouterLink>
        </fieldset>
    </div>
</template>

<script setup>
</script>

<style scoped>
</style>