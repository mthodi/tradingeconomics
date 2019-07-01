<template>
  <div class="app">
    <div v-if="loading" class="loading">
      Loading graph data...
    </div>
    <div v-if="error" class="error white--text">
      Something went wrong. Try reloading the page.
    </div>
    <div v-if="series">
      <apexcharts ref="index-graph" width="100%" type="area" :options="chartOptions" :series="series"></apexcharts>
    </div>
  </div>
</template>

<script>
  import VueApexCharts from "vue-apexcharts";
  import axios from "axios";
  import {
    API_URL
  } from '../_config'
  
  export default {
    name: "IndexGraph",
    components: {
      apexcharts: VueApexCharts
    },
    data: function() {
      return {
        chartOptions: {
          chart: {
            id: "index-chart"
          },
          xaxis : {
            type : 'datetime'
          },
          title: {
            text: "Performance of " + this.$route.query.symbol.split(':')[0],
            align: "center",
            margin: 10,
            offsetX: 0,
            offsetY: 0,
            floating: false,
            style: {
              fontSize: "16px",
              color: "black",
              fontWeight : "bold"
            }
          },
          dataLabels: {
            enabled: false,
            style: {
              colors: ['#fff']
            }
          },
          markers: {
            colors: ['black']
          },
          tooltip: {
            theme: "light"
          },
          legend: {
            show: true,
            horizontalAlign: 'right',
          }
        },
        series: null,
        loading : false,
        error : null

      };
    },
    //fetch data when component is created
    created() {
      this.fetchData()
    },
    //refetch data when the route changes
    watch: {
      '$route': 'fetchData'
    },
    methods: {
      fetchData() {
        this.error = this.series = null;
        this.loading = true;
        axios.get(API_URL + "/index/trend?symbol=" + this.$route.query.symbol)
          .then(response => {
            this.loading = false;
            //get the closing value and date
            const parsedData = response.data.map(s => {
              return {
                x : new Date(s.date),
                y: s.close
              };
            });
            //create the series
            this.series = [{
              name : "Close",
              data : parsedData
            }]
            //console.log(this.series)
          })
          .catch(e => {
            this.loading = false;
            this.error = e.toString();
            //console.log(this.error) // uncomment for debugging
          });
      }
    },

  };
</script>



