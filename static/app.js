const appConfig = {
    data() {
        return {
            tasks: [
                { id: 0, text: 'Learn JavaScript' },
                { id: 1, text: 'Learn Vue' },
                { id: 2, text: 'Build something awesome' }
            ]
        }
    }
}

const app = Vue.createApp(appConfig)

app.component('task-detail', {
    props: ['task'],
    template: `<li>{{ task.text }}</li>`
})

app.mount('#app')
