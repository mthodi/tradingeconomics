<template>
  <div class="content mt-3">
    <EPADescription />
    <div class="row">
      <div class="col-sm">
        <EPAProfile />
      </div>
      <div class="col-sm">
        <BarGraph/>
      </div>
    </div>
    <div class="row mt-1">
      <div class="col-sm">
        <AreaGraph />
      </div>
      <div class="col-sm">
        <Statistics />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import EPADescription from "@/components/EPADescription.vue";
import EPAProfile from "@/components/EPAProfile.vue";
import BarGraph from './BarGraph.vue';
import Statistics from "@/components/Statistics.vue";
import AreaGraph from './AreaGraph.vue';

export default {
  name: "Detailed",
  components: {
    EPAProfile,
    BarGraph,
    Statistics,
    AreaGraph,
    EPADescription
  }
};
</script>
