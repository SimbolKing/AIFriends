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
            <div v-if="$route.name === 'homepage-index'" class="navbar-center w-4/5 max-w-180 flex justify-center">
                <form @submit.prevent="handleSearch" class="join w-4/5 flex justify-center">
                    <input v-model="searchQuery" class="input join-item w-4/5" placeholder="Ask now" />
                    <button class="btn join-item gap-0">
                        <SearchIcon />
                    </button>
                </form>
            </div>
            <div class="navbar-end">
                <RouterLink v-if="!user.isLogin() && user.hasPulledUserInfo" :to="{name: 'user-account-login-index'}" class="mr-3 btn btn-ghost text-lg px-3">
                    Account
                </RouterLink>
                <UserMenu v-else-if="user.isLogin()" class="mr-3 mt-1" />
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
import { useRoute, useRouter } from 'vue-router';
import { ref, watch } from 'vue';

const user = useUserStore()

const searchQuery = ref('')
const router = useRouter()
const route = useRoute()

watch(() => route.query.q, newQ => {
  searchQuery.value = newQ || ''
})

function handleSearch() {
  router.push({
    name: 'homepage-index',
    query: {
      q: searchQuery.value.trim(),
    }
  })
}
</script>

<style scoped>
</style>