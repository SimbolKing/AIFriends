<script setup>
import api from '@/js/http/api';
import { useUserStore } from '@/stores/user';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const user = useUserStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const confirmedPassword = ref('')
const errorMessage = ref('')

async function handleRegister() {
    errorMessage.value = ''
    if (!username.value.trim()) {
        errorMessage.value = 'username can not be empty'
    } else if (!password.value.trim()) {
        errorMessage.value = 'password can not be empty'
    } else if (password.value.trim() !== confirmedPassword.value.trim()) {
        errorMessage.value = 'Please enter the same password'
    } else {
        try {
            const res = await api.post('/api/user/account/register/', {
                username: username.value,
                password: password.value,
            })
            const data = res.data
            if (data.result === 'success') {
                user.setAccessToken(data.access)
                user.setUserInfo(data)
                await router.push({name: 'homepage-index'})
            } else {
                errorMessage.value = data.result
            }
        } catch (err) {
        }
    }
}
</script>

<template>
    <div class="flex justify-center mt-30">
        <form @submit.prevent="handleRegister" class="fieldset bg-base-200 border-base-300 rounded-box w-md border p-4">

            <label class="label mx-auto w-5/6">Username</label>
            <input v-model="username" type="text" class="input mx-auto w-5/6" placeholder="Username" />

            <label class="label mx-auto w-5/6">Password</label>
            <input v-model="password" type="password" class="input mx-auto w-5/6" placeholder="Password" />

            <label class="label mx-auto w-5/6">Confirm your password</label>
            <input v-model="confirmedPassword" type="password" class="input mx-auto w-5/6" placeholder="Password" />

            <p v-if="errorMessage" class="text-sm text-red-500 mt-1 ml-9">{{ errorMessage }}</p>

            <button class="btn btn-neutral mt-4 mx-auto w-5/6">Register</button>
            <RouterLink :to="{name: 'user-account-login-index'}" class="btn btn-ghost mx-auto w-5/6">Login</RouterLink>
        </form>
    </div>
</template>

<style scoped>
</style>