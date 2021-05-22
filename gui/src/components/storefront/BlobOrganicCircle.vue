<template>
  <v-container>
    <v-row align="center">
      <v-col align-self="center" class="text-center" >
        <svg id="organic-blob" width="600" height="600" xmlns="http://www.w3.org/2000/svg" filter="url(#goo)">
          <defs>
            <filter id="goo">
              <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur"/>
              <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9"
                             result="goo"/>
              <feComposite in="SourceGraphic" in2="goo" operator="atop"/>
            </filter>
          </defs>
          <circle r="100" :class="[storeCapacityReached ? states.stop.colorClass : states.go.colorClass]" id="Circle1"></circle>
          <circle r="100" :class="[storeCapacityReached ? states.stop.colorClass : states.go.colorClass]" id="Circle2"></circle>
          <circle r="100" :class="[storeCapacityReached ? states.stop.colorClass : states.go.colorClass]" id="Circle3"></circle>
          <circle r="100" :class="[storeCapacityReached ? states.stop.colorClass : states.go.colorClass]" id="Circle4"></circle>
          <image class="logo" style="z-index: 100" height="300" width="300" x="150" y="150"  :href="storeCapacityReached ? states.stop.image : states.go.image"></image>
        </svg>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "BlobOrganicCircle",
  data() {
    return {
      storeCapacityReached: false,
      states: {
        stop: {
          image: require("@/assets/storefront/stop.png"),
          colorClass: "organic-blob-stop"
        },
        go: {
          image: require("@/assets/storefront/go.png"),
          colorClass: "organic-blob-go"
        },


      },
    }
  }
}
</script>

<style scoped>

.organic-blob-stop {
  fill: #E05858;
}

.organic-blob-go {
  fill: #66e058;
}


@keyframes from0to360 {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}

#Circle1 {
  animation: from0to360 2s linear infinite;
  cx: 300;
  cy: 290;
  r: 200;
  transform-origin: center;
}

@keyframes from360to0 {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}

#Circle2 {
  animation: from360to0 3s linear infinite;
  cx: 290;
  cy: 300;
  r: 200;
  transform-origin: center;
}

#Circle3 {
  animation: from0to360 4s linear infinite;
  cx: 280;
  cy: 290;
  r: 200;
  transform-origin: center;
}

#Circle4 {
  animation: from360to0 2.5s linear infinite;
  cx: 290;
  cy: 280;
  r: 200;
  transform-origin: center;
}
</style>
