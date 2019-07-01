<template>
 <v-layout>
    <div v-if="loading" class="loading">
      Loading news headlines...
    </div>
    <div v-if="error" class="error">
      Something went wrong. Please try reloading the page.
    </div>
    <div v-if="values">
      <v-toolbar flat color="white">
        <v-toolbar-title>News Headlines</v-toolbar-title>
      </v-toolbar>
      <v-data-table :headers="columns" :items="values" :expand="expand">
        <template v-slot:items="props">
          <tr @click="props.expanded = !props.expanded">
            <td> {{props.item.title}}</td>
          </tr>
        </template>
        <template v-slot:expand="props">
          <v-card color="blue-grey lighten-5" flat>
            <v-card-title>
              <div>
                Country : <span class="grey--text">{{props.item.country}}</span>
                &nbsp;
                Category: <span class="grey--text">{{props.item.category}}</span>
                <v-spacer></v-spacer>
                <span class="gray--text">{{props.item.date | moment('Do MMMM YYYY ')}}</span>
              </div>
            </v-card-title>
            <v-card-text>
              {{props.item.description}}
            </v-card-text>
            <v-card-actions>
              <v-btn flat :href="'https://www.tradingeconomics'+ props.item.url" color="blue">Read more on tradingeconomics</v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-data-table>
  </div>
 </v-layout>
</template>

<script>
import axios from 'axios';
import { API_URL } from '../_config'

export default {
  name: "NewsHeadlines",
  data() {
    return {
      columns: [
        {text: 'Click on headline to read more', value: 'title', sortable: false}
      ],
      expand: false,
      values: null,
      loading: false,
      error: null
    }
  },
  // Fetches posts when the component is created.
  created() {
    this.fetchData();
  },
  methods:{
    fetchData(){
      this.loading = true;
      axios.get(API_URL + '/news/')
      .then(response => {
        // JSON responses are automatically parsed.
        this.loading = false;
        this.values = response.data
      })
    .catch(e => {
      this.loading = false;
      this.error = e.toString()
      console.log(this.error);
    })
    }
  }
};
</script>
