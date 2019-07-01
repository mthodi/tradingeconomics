<template>
  <v-container>
    <div v-if="loading" class="loading">
      Loading index peers...
    </div>
    <div v-if="error" class="error">
      Something went wrong. Please try reloading the page.
    </div>
    <div v-if="values">
      <v-toolbar flat color="white">
        <v-toolbar-title>Performance of Index Peers</v-toolbar-title>
      </v-toolbar>
      <v-data-table :headers="columns" :items="values" class="elavation-1">
        <template v-slot:items="props">
            <td><router-link :to="'/index/'+ props.item.Ticker+ '?symbol='+ props.item.Symbol">{{ props.item.Ticker }}</router-link></td>
            <td>{{ props.item.Country }}</td>
            <td :class="[( props.item.Last > 0 ? 'green--text' : 'red--text')]">{{ props.item.Last }}</td>
            <td :class="[( props.item.DailyPercentualChange > 0 ? 'text-xs-justify green--text' : 'text-s-justify red--text')]">{{ props.item.DailyPercentualChange}}</td>
            <td :class="[( props.item.YTDPercentualChange > 0 ? 'text-xs-justify green--text' : 'text-xs-justify green--text')]">{{ props.item.YTDPercentualChange }}</td>
        </template>
      </v-data-table>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
import { API_URL } from '../_config'

export default {
  name: "PeerList",
  data() {
    return {
      columns: [
        { text: "Ticker", value: 'Ticker', sortable: true},
        { text: "Country", value: 'Country'},
        { text: "Current Value", value: 'Last'},
        { text: '%Change;',value: 'DailyPercentualChange'},
        { text: '% YTD',value: 'YTDPercentualChange'},
      ],
      values: null,
      loading: false,
      error: null
    }
  },
  // Fetches posts when the component is created.
  created() {
    this.fetchData()
  },
  methods:{
    fetchData(){
      this.values = this.error = null;
      this.loading = true;
      axios.get(API_URL + '/index/peers?symbol=' + this.$route.params.symbol)
    .then(response => {
      // JSON responses are automatically parsed.
      this.loading = false;
      this.values = response.data
    })
    .catch(e => {
      this.loading = false;
      this.error = e.toString();
      //console.log(this.error);
    })
    }
  }
};
</script>
