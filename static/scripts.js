
Vue.component(
    'v-table',
    {
  props: [ 'resources' ],
  data: function () {
            return {
            sortKey: 'name',
            search: '',
            reverse: false,
            page: 1,
            per_page: 20,
            }
  },

  methods: {
        sortBy: function(sortKey) {
              this.reverse = (this.sortKey == sortKey) ? ! this.reverse : false;

              this.sortKey = sortKey;
        },
        onchange() {
            this.page =  this.$refs.page.value;
            this.per_page = this.$refs.per_page.value;
        },
  },
  computed: {
        sortedresources: function () {
             return this.resources.sort((a, b) => {
                let modifier = 1;
                if(this.reverse) modifier = -1;
                if(a[this.sortKey] < b[this.sortKey]) return -1 * modifier;
                if(a[this.sortKey] > b[this.sortKey]) return 1 * modifier;
                return 0;
             });
        },
        slicedres: function () {
            first = ( this.page - 1 ) * this.per_page
            second = this.page * this.per_page
            return this.sortedresources.slice(first, second)
        },
        pages: function () {
            return (this.resources.length/this.per_page).toFixed()
        },
  },

  template: `
    <div>
    <input v-model="search" class="form-control" placeholder="Фильтр по названию, кол-ву или расстоянию">
    кол-во на странице<select name="per_page" ref="per_page" v-model="per_page">
        <option selected value=20>20</option><option value=40>40</option>
    </select>
    страница<select name="page" @change="onchange($event)"  ref="page" v-model="page" >
           <option v-for="inx in parseInt(pages)" :key="inx" >{{ inx }}</option>
    </select>
    <table border="1">
         <tr>
             <th>Дата</th>
             <th><a href="#" @click="sortBy('name')">Название</a></th>
             <th><a href="#" @click="sortBy('amount')">Количество</a></th>
             <th><a href="#" @click="sortBy('distance')">Расстояние</a></th>
         </tr>
        <tr v-for="res in slicedres">
            <td>{{ res.date }}</td>
            <td>{{ res.name }}</td>
            <td>{{ res.amount }}</td>
            <td>{{ res.distance }}</td>
        </tr>
        </table>
    </div>`
})

let app = new Vue({ el: '#app', data: {
    resources: [],
    },
    created: function () {
        axios.post("/", {
                        page: 1,
                        per_page: 60
                        }).then( res => (this.resources = res.data)
                        );
    },
    computed: {

    },
    methods: {

      	jsononchange(event) {
        	axios.post("/", {
                page: event.target.value,
                per_page: this.$refs.per_page.value
        	}).then( res => (this.resources = res.data) );
        }
    },
    })