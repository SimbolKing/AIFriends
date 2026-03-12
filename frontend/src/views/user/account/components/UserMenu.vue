<template>
    <div class="dropdown dropdown-end">
    <div tabindex="0" role="button" class="avatar btn btn-circle w-8 h-8 mr-6">
        <div class="w-8 rounded-full">
            <img :src="user.photo" alt="">
        </div>
    </div>
    <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-lg mt-5">
        <li>
            <RouterLink @click="closeMenu" :to="{name: 'user-space-index', params: {user_id: user.id}}">
                <div class="avatar">
                    <div class="w-10 rounded-full">
                        <img :src="user.photo" alt="">
                    </div>
                </div>
                <span class="text-base font-bold ml-1.5 line-clamp-1 break-all">{{ user.username }}</span>
            </RouterLink>
        </li>
        <li></li>
        <li>
            <RouterLink @click="closeMenu" :to="{name: 'user-space-index', params: {user_id: user.id}}" class="font-bold text-sm py-2.5">
                <UserSpaceIcon />
                My Space
            </RouterLink>
        </li>
        <li>
            <RouterLink @click="closeMenu" :to="{name: 'user-profile-index'}" class="font-bold text-sm py-2.5">
                <UserProfileIcon />
                My Profile
            </RouterLink>
        </li>
        <li></li>
        <li>
            <a @click="handleLogout" class="font-bold text-sm py-2.5">
                <UserLogoutIcon />
                Logout
            </a>
        </li>
    </ul>
    </div>
</template>

<script setup>
import UserLogoutIcon from '@/components/icons/UserLogoutIcon.vue';
import UserProfileIcon from '@/components/icons/UserProfileIcon.vue';
import UserSpaceIcon from '@/components/icons/UserSpaceIcon.vue';
import { useUserStore } from '@/stores/user';
import api from '@/utils/http/api';
import { useRouter } from 'vue-router';

const user = useUserStore()
const router = useRouter()

function closeMenu() {
    const element = document.activeElement
    if (element && element instanceof HTMLElement) element.blur()
}

async function handleLogout() {
    try {
        const res = await api.post('/api/user/account/logout/')
        if (res.data.result === 'success') {
            user.logout()
            await router.push({name: 'user-account-login-index'})
        }
    } catch(err) {
    }
}
</script>

<style scoped>
</style>