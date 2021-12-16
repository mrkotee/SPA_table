
Vue.component(
    'v-table',
    {
  props: [ 'resources', 'page', 'per_page' ],

  template: `<table border="1">
                         <tr>
                             <th>Дата</th>
                             <th>Название</th>
                             <th>Количество</th>
                             <th>Расстояние</th>
                         </tr>
        <tr v-for="res in resources">
            <td>{{ res.date }}</td>
            <td>{{ res.name }}</td>
            <td>{{ res.amount }}</td>
            <td>{{ res.distance }}</td>
        </tr>
        </table>`
})

let app = new Vue({ el: '#app', data: {
    page: 1,
    per_page: 20,
    resources: [],
    },
      created: function () {
            axios.post("/", {
                            page: 1,
                            per_page: this.per_page
                            }).then( res => (this.resources = res.data)
                            );
            console.log(this.resources);
      },
    methods: {
      	onchange(event) {
        	console.log(this.$refs.per_page);
        	axios.post("/", {
                page: event.target.value,
                per_page: this.$refs.per_page.value
        	}).then( res => (this.resources = res.data) );
        }
      },
    })