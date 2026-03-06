<script setup>
import { useUserStore } from '@/stores/user';
import UserSpaceIcon from './icons/UserSpaceIcon.vue';
import UserProfileIcon from './icons/UserProfileIcon.vue';
import UserLogoutIcon from './icons/UserLogoutIcon.vue';
import api from '@/js/http/api';
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
            await router.push({name: 'homepage-index'})
        }
    } catch (err) {
    }
}
</script>

<template>
    <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="avatar btn btn-circle w-11 h-11 mr-0">
            <div class="w-8 rounded-full">
                <img :src="user.photo" alt="">
            </div>
        </div>
        <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-48 p-2 shadow-sm mt-3">
            <li>
                <RouterLink @click="closeMenu" :to="{name: 'user-space-index', params: {user_id: user.id}}">
                    <div class="avatar">
                        <div class="w-10 rounded-full">
                            <img :src="user.photo" alt="">
                        </div>
                    </div>
                    <div class="text-base font-bold line-clamp-1 break-all">{{ user.username }}</div>
                </RouterLink>
            </li>
            <li></li>
            <li>
                <RouterLink @click="closeMenu" :to="{name: 'user-space-index', params: {user_id: user.id}}" class="text-sm font-bold py-2.5">
                    <UserSpaceIcon />
                    My Space
                </RouterLink>
            </li>
            <li>
                <RouterLink @click="closeMenu" :to="{name: 'user-profile-index'}" class="text-sm font-bold py-2.5">
                    <UserProfileIcon />
                    Edit Profile
                </RouterLink>
            </li>
            <li></li>
            <li>
                <a @click="handleLogout" class="text-sm font-bold py-2.5">
                    <UserLogoutIcon />
                    Logout
                </a>
            </li>
        </ul>
    </div>
</template>

<style scoped>
</style>