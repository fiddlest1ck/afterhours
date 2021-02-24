<template>
  <v-app>
    <v-row>
    <v-col>
      <v-sheet height="400">
        <v-calendar
          :events=events
          :event-color='getEventColor'
          type="day"
          locale="pl"
        >
        <template v-slot:event="{ event }">
          <div>
            {{event.name}}
          </div>
        </template>
        </v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
  </v-app>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  name: 'App',
  data() {
    return {
      events: []
    };
  },
  created() {
    axios
      .get('/api/v1/callendar')
      .then(response => (this.getEvents(response.data)))
    },
    methods: {
      getEvents(data) {
        return data.map(data => {
          this.events.push({
            name: `${data.hour}`,
            start: `${moment().format('YYYY-MM-DD')} ${data.hour}`,
            end: `${moment().format('YYYY-MM-DD')} ${data.hour}`,
            color: data.color
          })})
      },
      getEventColor(event) {
        return event.color
      }
    }
  }
</script>
