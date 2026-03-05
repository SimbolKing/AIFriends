<script setup>
</script>

<template>
    <div class="flex justify-center mt-30">
        <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-md border p-4">

            <label class="label mx-auto w-5/6">Username</label>
            <input type="text" class="input mx-auto w-5/6" placeholder="Username" />

            <label class="label mx-auto w-5/6">Password</label>
            <input type="password" class="input mx-auto w-5/6" placeholder="Password" />

            <button class="btn btn-neutral mt-4 w-5/6 mx-auto">Login</button>
            <RouterLink :to="{name: 'user-account-register-index'}" class="btn btn-ghost w-5/6 mx-auto">Register</RouterLink>
        </fieldset>
    </div>
</template>

<style scoped>
</style>