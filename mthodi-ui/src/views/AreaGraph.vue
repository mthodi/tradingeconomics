<template>
  <div class="app">
    <apexcharts ref="areagraph" width="95%" type="line" :options="chartOptions" :series="series"></apexcharts>
  </div>
</template>

<script>
  import VueApexCharts from "vue-apexcharts";
  import axios from "axios";
  import {
    API_URL
  } from '../_config'
  
  export default {
    name: "AreaGraph",
    components: {
      apexcharts: VueApexCharts
    },
    data: function() {
      return {
        chartOptions: {
          chart: {
            id: "rainfall-chart"
          },
          yaxis: {
            tickAmount: 3,
            title : {
              text : "Amount"
            },
            labels: {
              formatter: function (value) {
                      return value + " mm";
              }
            }
          },
          xaxis: {
            type: 'datetime',
            tickAmount: 3,
            // labels: {
            //   // formatter: function (value) {
            //   //         var tmp = new Date(value);
            //   //         return tmp.getDate() + '-' + tmp.getMonth() + '-' + tmp.getFullYear()
            //   // }
            //   format : 'DD/MM'
            // }
          },
          title: {
            text: "Daily rainfall",
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
          plotOptions: {
            bar: {
              horizontal: false,
            },
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
        series: [],
        // xaxis: {
        //       type: 'category',
        //       // categories : []
        //   }

      };
    },
    created() {
      this.fetchData()
    },
    watch: {
      '$route': 'fetchData'
    },
    methods: {
      fetchData() {
        axios.get(API_URL + "/epa/trends?name=" + this.$route.params.name)
          .then(response => {
            this.series = response.data;
            //this.$refs['graph'].updateOptions({xaxis: {categories : response.data[0].categories}})
            //this.xaxis.categories = response.data[0].categories;
            console.log(response.data)
          })
          .catch(e => {
            this.loading = false;
            this.error = e;
            console.log(e)
          });
      }
    },

  };
</script>



