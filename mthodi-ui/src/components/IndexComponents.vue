<template>
  <div class="col">
    <div v-if="loading" class="loading">Loading Index components...</div>
    <div v-if="error" class="error white--text">Something went wrong. Please try reloading the page.</div>
    <div v-if="values" class="row">
      <v-app id="table">
      <v-toolbar flat color="white">
        <h2>Index Components</h2>
        <v-spacer></v-spacer>
        <!-- A search box for data in table-->
        <v-text-field  v-model="search" append-icon="search" label="Search an index component" single-line hide-details width="50%">
        </v-text-field>
      </v-toolbar>
        <v-data-table :headers="columns" :items="values" :search="search" class="elevation-1">
          <template v-slot:items="props">
            <td>{{props.item.Ticker}}</td>
            <td class="text-xs-right">{{ props.item.Last }}</td>
            <td :class="[( props.item.DailyChange > 0 ? 'green white--text' : 'red darken-4 white--text')]">{{ props.item.DailyChange }}</td>
            <td :class="[( props.item.DailyPercentualChange > 0 ? 'green white--text' : 'red darken-4 white--text')]">{{ props.item.DailyPercentualChange }}</td>
            <td :class="[( props.item.WeeklyPercentualChange > 0 ? 'green white--text' : 'red darken-4 white--text')]">{{ props.item.WeeklyPercentualChange }}</td>
            <td :class="[( props.item.MonthlyPercentualChange > 0 ? 'green white--text' : 'red darken-4 white--text')]">{{ props.item.MonthlyPercentualChange }}</td>
            <td :class="[( props.item.YTDPercentualChange > 0 ? 'green white--text' : 'red darken-4 white--text')]">{{ props.item.YTDPercentualChange }}</td>
          </template>
          <!-- Slot shown when server returns no data. -->
          <template v-slot:no-data>
            <v-alert :value="true"  color="error">
              Sorry, the server did not return any data for this index.
            </v-alert>
          </template>
          <!-- Slot shown when search returns no results -->
          <template v-slot:no-results>
            <v-alert :value="true"  color="error">
              Sorry, that stock was not found in this index.
            </v-alert>
          </template>
        </v-data-table>
      </v-app>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { API_URL } from "../_config";

export default {
  name: "IndexComponents",
  data() {
    return {
      search: '',
      values: null,
      loading: false,
      error: null,
      columns: [
        { text: "Ticker", value: "Ticker", sortable: true },
        { text: "Close", value: "Last" },
        { text: "Change", value: "DailyChange" },
        { text: "%Change", value: "DailyPercentualChange" },
        { text: "%Weekly", value: "WeeklyPercentualChange" },
        { text: "%Monthly", value: "MonthlyPercentualChange" },
        { text: "% YTD", value: "YTDPercentualChange" }
      ]
    };
  },
  // Fetches posts when the component is created.
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.error = this.values = null;
      this.loading = true;
      axios
        .get(API_URL + "/index/?symbol=" + this.$route.query.symbol)
        .then(response => {
          // JSON responses are automatically parsed.
          this.loading = false;
          this.values = response.data;
        })
        .catch(e => {
          this.loading = false;
          this.error = "Something went wrong. Please try reloading the page.";
          //console.log(this.error)
        });
    }
  }
};
</script>

