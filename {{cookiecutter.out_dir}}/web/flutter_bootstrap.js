{{ '{{flutter_js}}' }}
{{ '{{flutter_build_config}}' }}

var config = {};
if (globalThis.webRenderer != "auto") {
    config.renderer = globalThis.webRenderer;
}
if (globalThis.canvasKitBaseUrl) {
    config.canvasKitBaseUrl = globalThis.canvasKitBaseUrl;
}

_flutter.loader.load({
    config: config,
    serviceWorkerSettings: {
        serviceWorkerVersion: {{ '{{flutter_service_worker_version}}' }},
    },
    onEntrypointLoaded: async function (engineInitializer) {
        const appRunner = await engineInitializer.initializeEngine({useColorEmoji: useColorEmoji});
        await appRunner.runApp();
    }
});