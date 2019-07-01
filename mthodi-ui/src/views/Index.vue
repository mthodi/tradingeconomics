<template>
  <div class="container mt-3 mb-3">
    <p class="bg-secondary mb-0 text-center">
          <!-- <small class="text-white"> -->
            <em> Click on the EPA NAme for more details.</em></p>
        
    <table class="table table-hover">
      <thead>
        <tr>
          <!-- <th scope="col">
             Country
          </th> -->
          <th scope="col"> EPA Name </th>
          <!-- <th scope="col">
            Name
          </th> -->
          <th scope="col"> EPS </th>
          <th scope="col">ROE</th>
          <th scope="col">ROA</th>
          <th scope="col">P/E</th>
          <th scope="col">P/S</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="value in values" :key="value.close">
          <!-- <td>{{ value.country }}</td> -->
          <td> <router-link :to="'/ratios/'+ value.ticker">{{ value.ticker }}</router-link></td>
          <!-- <td>{{ value.company_name }}</td> -->
          <td>{{ value.EPS | abbreviate }}</td>
          <td>{{ value.ROE | percentage }}</td>
          <td>{{ value.ROA | percentage }}</td>
          <td>{{ value.PE }}</td>
          <td>{{ value.PS }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import { API_URL } from '../_config'

export default {
  name: "Index",
  data() {
    return {
      values: [],
      errors: []
    }
  },
  // Fetches posts when the component is created.
  created() {
    axios.get(API_URL + "/api/v1/ratios/all")
    .then(response => {
      // JSON responses are automatically parsed.
      this.values = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
};
</script>
