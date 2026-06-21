// static/sw.js
// Place this file at the ROOT of your static folder: static/sw.js
// It must also be served from the ROOT of your site: /sw.js
// Add this to your main urls.py to serve it correctly (see instructions below)

const CACHE_NAME = 'e-lecturer-v1';

// ── Install ──────────────────────────────────────────────────
self.addEventListener('install', event => {
    self.skipWaiting();
});

// ── Activate ─────────────────────────────────────────────────
self.addEventListener('activate', event => {
    event.waitUntil(clients.claim());
});

// ── Push received ────────────────────────────────────────────
self.addEventListener('push', event => {
    let data = { title: 'E-Lecturer', body: 'You have a new notification', url: '/dashboard/' };

    if (event.data) {
        try { data = JSON.parse(event.data.text()); } catch (e) {}
    }

    const options = {
        body:    data.body,
        icon:    data.icon || '/static/icons/icon-192.png',
        badge:   '/static/icons/badge-72.png',
        vibrate: [200, 100, 200],
        data:    { url: data.url || '/dashboard/' },
        actions: [
            { action: 'open',    title: '📖 Open App' },
            { action: 'dismiss', title: '✕ Dismiss'  },
        ],
    };

    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});

// ── Notification click ───────────────────────────────────────
self.addEventListener('notificationclick', event => {
    event.notification.close();

    if (event.action === 'dismiss') return;

    const url = event.notification.data?.url || '/dashboard/';

    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then(clientList => {
            // If app is already open, focus it
            for (const client of clientList) {
                if (client.url.includes(self.location.origin) && 'focus' in client) {
                    client.navigate(url);
                    return client.focus();
                }
            }
            // Otherwise open a new tab
            if (clients.openWindow) return clients.openWindow(url);
        })
    );
});
