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
            <div class="navbar-center w-4/5 max-w-180">
                <div class="join w-4/5">
                    <input class="input join-item w-4/5" placeholder="Ask now" />
                    <button class="btn join-item gap-0">
                        <SearchIcon />
                        Search
                    </button>
                </div>
            </div>
            <div class="navbar-end">
                <button class="btn btn-ghost text-lg">Account</button>
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
                <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5" data-tip="Homepage">
                    <HomepageIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Homepage</span>
                </button>
            </li>
            <li>
                <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5" data-tip="Friend">
                    <FriendIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Friend</span>
                </button>
            </li>
            <li>
                <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-2.5" data-tip="Create">
                    <CreateIcon />
                    <span class="is-drawer-close:hidden text-base ml-1 whitespace-nowrap">Create</span>
                </button>
            </li>
        </ul>
        </div>
    </div>
    </div>
</template>

<script setup>
import CreateIcon from '../icons/CreateIcon.vue';
import FriendIcon from '../icons/FriendIcon.vue';
import HomepageIcon from '../icons/HomepageIcon.vue';
import MenuIcon from '../icons/MenuIcon.vue';
import SearchIcon from '../icons/SearchIcon.vue';

</script>

<style scoped>
</style>