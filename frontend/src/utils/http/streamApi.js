import { fetchEventSource } from '@microsoft/fetch-event-source';
import { useUserStore } from "@/stores/user.js";
import api from './api';

const BASE_URL = 'http://127.0.0.1:8000'

export default async function streamApi(url, options = {}) {
    const userStore = useUserStore();

    const startFetch = async () => {
        return await fetchEventSource(BASE_URL + url, {
            method: options.method || 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${userStore.accessToken}`,
                ...options.headers,
            },
            body: JSON.stringify(options.body || {}),

            openWhenHidden: true,
            async onopen(response) {
                if (response.status === 401) {
                    try {
                        await api.post('/api/user/account/refresh_token/', {});
                        throw new Error("TOKEN_REFRESHED");
                    } catch (err) {
                        throw err;
                    }
                }

                if (!response.ok || !response.headers.get('content-type')?.includes('text/event-stream')) {
                    const errorData = await response.json().catch(() => ({}));
                    throw new Error(errorData.detail || `Request failed: ${response.status}`);
                }
            },

            onmessage(msg) {
                if (msg.data === '[DONE]') {
                    if (options.onmessage) options.onmessage('', true);
                    return
                }
                try {
                    const json = JSON.parse(msg.data);
                    if (options.onmessage) options.onmessage(json, false);
                } catch (e) {
                    console.error("Stream parsing failed:", e);
                }
            },

            onerror(err) {
                if (err.message === "TOKEN_REFRESHED") {
                    return startFetch();
                }

                if (options.onerror) {
                    options.onerror(err);
                }
                throw err;
            },

            onclose: options.onclose,
        });
    };

    return await startFetch();
}
