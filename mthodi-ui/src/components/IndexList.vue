<template>
  <v-container fluid>
     <div v-if="loading" class="loading">
      Loading market indices...
    </div>
    <div v-if="error" class="error white--text">
      Something went wrong. Please try reloading the page.
    </div> 
    <div v-if="values">
      <v-toolbar flat color="white">
        <v-toolbar-title>Market Indices<h6 class="grey--text"> Click on Ticker for more details</h6></v-toolbar-title>
      </v-toolbar>
      <v-data-table :headers="columns" :items="values" class="elavation-1">
        <template v-slot:items="props">
            <td><router-link :to="'/index/'+ props.item.Ticker+ '?symbol='+ props.item.Symbol">{{ props.item.Ticker }}</router-link></td>
            <td>{{ props.item.Name }}</td>
            <td>{{ props.item.Country }}</td>
            <td :class="[( props.item.Last > 0 ? 'green--text' : 'red--text')]">{{ props.item.Last }}</td>
            <td :class="[( props.item.DailyChange > 0 ? 'green--text' : 'text-s-justify red--text')]">{{ props.item.DailyChange}}</td>
            <td :class="[( props.item.DailyPercentualChange > 0 ? 'text-xs-justify green--text' : 'text-s-justify red--text')]">{{ props.item.DailyPercentualChange}}</td>
            <td :class="[( props.item.MonthlyPercentualChange > 0 ? 'text-xs-justify green--text' : 'text-s-justify red--text text-white')]">{{ props.item.MonthlyPercentualChange}}</td>
            <td :class="[( props.item.YTDPercentualChange > 0 ? 'text-xs-justify green--text' : 'text-xs-justify green--text')]">{{ props.item.YTDPercentualChange }}</td>
            <td>{{  props.item.Date | moment("DD-MM-YYYY") }}</td>
        </template>
      </v-data-table>
    </div>
  </v-container>
</template>


<script>
import axios from 'axios';
import { API_URL } from '../_config'

export default {
  name: "IndexList",
  data() {
    return {
      values : null,
      loading : false,
      error: null,
      //table columns
      columns: [
          { text: 'Ticker', value: 'Ticker', sortable: true},
          { text: 'Index Name', value: 'Name'},
          { text: 'Country',value: 'Last'},
          { text: 'Close',value: 'Last'},
          { text: 'Change',value: 'DailyChange'},
          { text: '%Change',value: 'DailyPercentualChange'},
          { text: '%Monthly',value: 'MonthlyPercentualChange'},
          { text: '% YTD',value: 'YTDPercentualChange'},
          { text: 'Updated on',value: 'Date'}
      ]
    }
  },
  // Fetches posts when the component is created.
  created() {
    this.fetchData()
  },
  methods: {
    fetchData(){
      this.error = this.values = null;
      this.loading = true;
      axios.get(API_URL)
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
