<script setup>
import { RouterView, useRoute, useRouter } from 'vue-router'
import NarBar from './components/navbar/NarBar.vue';
import { onMounted } from 'vue';
import api from './js/http/api';
import { useUserStore } from './stores/user';

const user = useUserStore()
const route = useRoute()
const router = useRouter()

onMounted(async () => {
  try {
    const res = await api.get('/api/user/account/get_user_info/')
    const data = res.data
    if (data.result === 'success') {
      user.setUserInfo(data)
    }
  } catch (err) {
  } finally {
    user.setHasPulledUserInfo(true)
    if (route.meta.needLogin && !user.isLogin()) {
      await router.replace({
        name: 'user-account-login-index'
      })
    }
  }
})
</script>

<template>
  <NarBar>
    <RouterView />
  </NarBar>
</template>

<style scoped>
</style>
