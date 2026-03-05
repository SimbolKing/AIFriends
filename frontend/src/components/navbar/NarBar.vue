<script setup>
import CreateIcon from './icons/CreateIcon.vue';
import FriendIcon from './icons/FriendIcon.vue';
import HomepageIcon from './icons/HomepageIcon.vue';
import MenuIcon from './icons/MenuIcon.vue';
import SearchIcon from './icons/SearchIcon.vue';

</script>

<template>
<div class="drawer lg:drawer-open">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <nav class="navbar w-full bg-base-100 shadow-sm">
        <div class="navbar-start">
            <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
            <MenuIcon />
        </label>
        <div class="px-2 font-bold text-xl">AI Friends</div>
        </div>
        <div class="navbar-center w-4/5 max-w-180 flex justify-center">
            <div class="join w-4/5 flex justify-center">
                <input class="input join-item rounded-l-full" placeholder="Search with AI Friends" />
                <button class="btn join-item rounded-r-full gap-0">
                    <SearchIcon />
                    Search
                </button>
            </div>
        </div>
        <div class="navbar-end mr-7">
            <RouterLink active-class="btn-active" :to="{name: 'user-account-login-index'}" class="btn btn-ghost text-lg">Account</RouterLink>
        </div>
    </nav>
    <slot></slot>
  </div>

  <div class="drawer-side is-drawer-close:overflow-visible">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-54">
      <ul class="menu w-full grow">
        <li>
          <RouterLink :to="{name: 'homepage-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3" data-tip="Homepage">
            <HomepageIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Home</span>
          </RouterLink>
        </li>
        <li>
          <RouterLink :to="{name: 'friend-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3" data-tip="Friends">
            <FriendIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Friends</span>
          </RouterLink>
        </li>
        <li>
          <RouterLink :to="{name: 'create-index'}" active-class="menu-focus" class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3" data-tip="Create">
            <CreateIcon />
            <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap">Create</span>
          </RouterLink>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>