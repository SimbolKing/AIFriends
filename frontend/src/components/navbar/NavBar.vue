<template>
    <div class="drawer lg:drawer-open">
    <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
        <nav class="navbar w-full bg-base-100 shadow-sm">
            <div class="navbar-start">
                <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
                    <MenuIcon />
                </label>
                <div class="px-2 font-bold text-lg">AI Friends</div>
            </div>
            <div v-if="$route.name !== 'user-account-login-index' && $route.name !== 'user-account-register-index'" class="navbar-center w-4/5 max-w-180 flex justify-center">
                <div class="join w-4/5 flex justify-center">
                    <input class="input join-item w-4/5" placeholder="Ask now" />
                    <button class="btn join-item gap-0">
                        <SearchIcon />
                        Search
                    </button>
                </div>
            </div>
            <div class="navbar-end">
                <RouterLink v-if="user.isLogin()" :to="{name: 'update-character', params: {character_id: 1}}" class="btn btn-ghost mr-5 px-2">
                    <CreateIcon />
                </RouterLink>
                <RouterLink v-if="!user.isLogin() && user.hasPulledUserInfo" :to="{name: 'user-account-login-index'}" class="mr-3 btn btn-ghost text-lg px-3">
                    Account
                </RouterLink>
                <UserMenu v-else-if="user.isLogin()" class="mr-3" />
            </div>
        </nav>
        <div class="p-4">
            <slot></slot>
        </div>
    </div>

    <div class="drawer-side is-drawer-close:overflow-visible">
        <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
        <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-54">
        <ul class="menu w-full grow">
            <li>
                <RouterLink :to="{name: 'homepage-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5 mb-1.5" data-tip="Homepage">
                    <HomepageIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Homepage</span>
                </RouterLink>
            </li>
            <li>
                <RouterLink :to="{name: 'friend-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5 mb-1.5" data-tip="Friend">
                    <FriendIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Friend</span>
                </RouterLink>
            </li>
            <li>
                <RouterLink :to="{name: 'create-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5 mb-1.5" data-tip="Create">
                    <CreateIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Create</span>
                </RouterLink>
            </li>
        </ul>
        </div>
    </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import CreateIcon from '../icons/CreateIcon.vue';
import FriendIcon from '../icons/FriendIcon.vue';
import HomepageIcon from '../icons/HomepageIcon.vue';
import MenuIcon from '../icons/MenuIcon.vue';
import SearchIcon from '../icons/SearchIcon.vue';
import UserMenu from '@/views/user/account/components/UserMenu.vue';

const user = useUserStore()
</script>

<style scoped>
</style>