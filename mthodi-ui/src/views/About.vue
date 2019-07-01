<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">About this application </h3>
            <div> {{ card_text }} </div>
          </div>
        </v-card-title>

        <v-card-actions>
          <v-btn flat color="orange" href="https://www.linkedin.com/in/martin-thodi/">Learn more about me</v-btn>
          <v-btn flat color="orange" href="https://github.com/mthodi/tradingeconomics">See this app on GitHub</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'About',
    data () {
      return {
        card_text: 'This was made by Martin Thodi for review by the Trading Economics Recruitment team.'
      }
    }
  }
</script>