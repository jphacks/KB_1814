<template>
<div class="all">
<!-- Q1 -->
  <div v-show="show1" class="transition">
    <div> <!-- Q -->
      <img class="Q_title" src="../assets/Q1.svg" width="100"/>
      <div class="Q">
        <img src="../assets/Qimage.svg" />
        <p> スタート地点はどこにする？ </p>
      </div>
    </div>
    <div> <!-- A -->
      <div class="A1" @click="Q1_method(0)">
        <img v-if = "Q1_active1" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
        <p> 京都。 </p>
      </div>
      <div class="A2" @click="Q1_method(1)">
        <img v-if = "Q1_active2" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
        <p> 大阪！ </p>
      </div>
      <div class="A3" @click="Q1_method(2)">
        <img v-if = "Q1_active3" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
        <p> 神戸！！ </p>
      </div>
    </div>
    <!-- next -->
    <img class="next" src="../assets/next+image.svg" @click="show2 = !show2" />
  </div>
  <!-- Q2 -->
    <div v-show="show2" class="transition">
      <div> <!-- Q -->
        <img class="Q_title" src="../assets/Q2.svg" width="100"/>
        <div class="Q">
          <img src="../assets/Qimage.svg" />
          <p> いつ行くの？ </p>
        </div>
      </div>
      <div> <!-- A -->
      <!-- 日付選択 -->
        <el-date-picker
          v-model="value1"
          type="date"
          placeholder="Pick a day"
          padding= "30px">
        </el-date-picker>
        <div class="A1" @click="Q2_method(0)">
          <img v-if = "Q2_active1" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
          <p> 朝 </p>
        </div>
        <div class="A2" @click="Q2_method(1)">
          <img v-if = "Q2_active2" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
          <p> 昼 </p>
        </div>
        <div class="A3" @click="Q2_method(2)">
          <img v-if = "Q2_active3" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
          <p> 夕 </p>
        </div>
        <div class="A2" @click="Q2_method(3)">
          <img src="../assets/A1.svg" />
          <p> 晩 </p>
        </div>
      </div>
    </div>
<!-- Q3 -->
  <div v-show="show3" class="transition">
    <div> <!-- Q -->
      <img class="Q_title" src="../assets/Q3.svg" width="100"/>
      <div class="Q">
        <img src="../assets/Qimage.svg" />
        <p> どれくらいお出かけに対して本気？ </p>
      </div>
    </div>
    <div> <!-- A -->
      <div class="A1" @click="Q3_method(0)">
        <img v-if = "Q3_active1" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
        <p> ゆったりかなあ </p>
      </div>
      <div class="A2" @click="Q3_method(1)">
        <img v-if = "Q3_active2" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
        <p> アクティブに外出！ </p>
      </div>
      <div class="A3" @click="Q3_method(2)">
        <img v-if = "Q3_active2" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
        <p> テンション高いけどインドア系で！ </p>
      </div>
    </div>
  </div>

  <!-- Q4 -->
    <div v-show="show4" class="transition" >
      <div> <!-- Q -->
        <img class="Q_title" src="../assets/Q4.svg" width="100"/>
        <div class="Q">
          <img src="../assets/Qimage.svg" />
          <p> じゃあこの中のどれが良いかしら？ </p>
        </div>
      </div>
      <div> <!-- A -->
        <div class="A1" @click="Q4_method(0)">
          <img v-if = "Q4_active1" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
          <p> ご飯 </p>
        </div>
        <div class="A2" @click="Q4_method(1)">
          <img v-if = "Q4_active2" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
          <p> 観光 </p>
        </div>
        <div class="A3" @click="Q4_method(2)">
          <img v-if = "Q4_active3" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
          <p> スポーツ </p>
        </div>
      </div>
      <!-- next -->
    <img class="next" src="../assets/next+image.svg" @click="show5 = !show5" />

    </div>
    <!-- Q5 -->
      <div v-show="show5" class="transition" >
        <div> <!-- Q -->
          <img class="Q_title" src="../assets/Q5.svg" width="100"/>
          <div class="Q">
            <img src="../assets/Qimage.svg" />
            <p> ちなみに予算は？ </p>
          </div>
        </div>
        <div> <!-- A -->
          <div class="A1" @click="Q5_method(3000)">
            <img v-if = "Q5_active1" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
            <p> 節約で…（¥3,000） </p>
          </div>
          <div class="A2" @click="Q5_method(10000)">
            <img v-if = "Q5_active2" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
            <p> 普通。 （¥10,000）</p>
          </div>
          <div class="A3" @click="Q5_method(50000)">
            <img v-if = "Q5_active3" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
            <p> ☆GOYU☆（¥50,000） </p>
          </div>
        </div>
      </div>
      <!-- Q5-2 -->
        <div v-show="show10" class="transition" >
          <div> <!-- Q -->
            <img class="Q_title" src="../assets/Q5-2.svg" width="100"/>
            <div class="Q">
              <img src="../assets/Qimage.svg" />
              <p> ご飯の予算は？ </p>
            </div>
          </div>
          <div> <!-- A -->
            <div class="A1" @click="Q5_method(3000)">
              <img v-if = "Q5_active12" src="../assets/A1_active.svg" />
        <img v-else src="../assets/A1.svg"/>
              <p> チープ </p>
            </div>
            <div class="A2" @click="Q5_method(10000)">
              <img v-if = "Q5_active22" src="../assets/A2_active.svg" />
        <img v-else src="../assets/A2.svg"/>
              <p> 普通 </p>
            </div>
            <div class="A3" @click="Q5_method(50000)">
             <img v-if = "Q5_active33" src="../assets/A3_active.svg" />
        <img v-else src="../assets/A3.svg"/>
              <p> 豪華 </p>
            </div>
          </div>
        </div>
        <!-- Q7 -->
          <div v-show="show6" class="transition" >
            <div> <!-- Q -->
              <img class="Q_title" src="../assets/Q6.svg" width="100"/>
              <div class="Q">
                <img src="../assets/Qimage.svg" />
                <p> 最後に移動手段ね。 </p>
              </div>
            </div>
            <div> <!-- A -->
              <div class="A1" @click="Q6_method(0)">
                <img src="../assets/A1.svg" />
                <p> 徒歩</p>
              </div>
              <div class="A2" @click="Q6_method(1)">
                <img src="../assets/A2.svg" />
                <p> 電車 </p>
              </div>
              <div class="A3" @click="Q6_method(2)">
                <img src="../assets/A3.svg" />
                <p> 車 </p>
              </div>
            </div>
          </div>
       <p v-show="show7" class="send" @click="post">Let's plan !</p>

        <div v-show="show8"><p> こんなプランはいかが？ </p>
        <div>
    <div
      id="map"
      :style="{width: mapWidth + 'px',height: mapHeight + 'px'}"/>
  </div>
          <div class="result" v-show="show8">
            <p class="time"><font color="#b3b3b3">1.</font>&emsp;{{result[0].Name}}</p>
            <p>{{result[0].OpeningHours}}</p>
           </div>
           <div class="result">
            <p class="time"><font color="#b3b3b3">2.</font>&emsp;{{result[1].Name}} </p>
            <p>{{result[1].OpeningHours}}</p>
          </div>
          <div class="result">
            <p class="time"><font color="#b3b3b3">3.</font>&emsp;{{result[2].Name}}</p>
            <p>{{result[2].OpeningHours}}</p>
          </div>
          </div>
</div>
</template>

<script>
   let GoogleMapsLoader = require("google-maps");

    GoogleMapsLoader.KEY = "AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8";
    GoogleMapsLoader.LANGUAGE = "ja";

    export default {
    name: "Gmap",
  props: {
    mapWidth: {
      type: Number,
      default: 500
    },
    mapHeight: {
      type: Number,
      default: 500
    },
    lat: {
      type: Number,
      default: 34.722677
    },
    lng: {
      type: Number,
      default: 135.492364
    },
    zoom: {
      type: Number,
      default: 8
    },
    markers: {
      type: Array,
      default: () => {
        return [];
      }
    }
  },

    data(){
      return{
        date:{
            region:[],
            date:null,
            time:[],
            tension:null,
            play:[],
            budget:null,
            move:null,
        },
        result:[{},{},{}]
        ,
        show1:true,
        show2:false,
        show3:false,
        show4:false,
        show5:false,
        show6:false,
        show7:false,
        show8:false,
        show9:false,
        show10:false,
        Q1_active1:false,
        Q1_active2:false,
        Q1_active3:false,
        Q2_active1:false,
        Q2_active2:false,
        Q2_active3:false,
        Q3_active1:false,
        Q3_active2:false,
        Q3_active3:false,
        Q4_active1:false,
        Q4_active2:false,
        Q4_active3:false,
        Q5_active1:false,
        Q5_active2:false,
        Q5_active3:false,
        Q5_active12:false,
        Q5_active22:false,
        Q5_active33:false,
        value1: '',

        map: null,
      formattedMarkers: []
        }
    },
    watch: {
    markers() {
      // マーカーを全削除
      this.formattedMarkers.forEach(marker => {
        marker.setMap(null);
      });
      // propsからも削除
      this.formattedMarkers.splice(0, this.formattedMarkers.length);

      // 再描画
      this.addMarker();
    }
  },
  created() {},
  mounted() {
    // googleMap描画
    GoogleMapsLoader.load(this.loadMap);
  },
    methods:{
        Q1_method(region_id){
            if(this.date.region.indexOf(region_id)== -1){
                 this.date.region.push(region_id)
                 if(region_id == 0){
                     this.Q1_active1 = true
                 }
                 else if (region_id == 1){
                     this.Q1_active2 = true
                 }
                 else{
                     this.Q1_active3 = true
                 }
            }
            else{
                var target = this.date.region.indexOf(region_id)
                this.date.region.splice(target,1)
                if(region_id == 0){
                     this.Q1_active1 =false
                 }
                 else if (region_id == 1){
                     this.Q1_active2 = false
                 }
                 else{
                     this.Q1_active3 = false
                 }
            }
            console.log("region"+this.date.region)
            
        },
        Q2_method(date_id){
            if(this.date.time.indexOf(date_id)== -1){
                 this.date.time.push(date_id)
                 if(date_id == 0){
                     this.Q2_active1 =true
                 }
                 else if (date_id == 1){
                     this.Q2_active2 = true
                 }
                 else{
                     this.Q2_active3 = true
                 }
            }
            else{
                var target = this.date.time.indexOf(date_id)
                this.date.time.splice(target,1)
                 if(date_id == 0){
                     this.Q2_active1 =false
                 }
                 else if (date_id == 1){
                     this.Q2_active2 = false
                 }
                 else{
                     this.Q2_active3 = false
                 }
            }
            console.log("time"+this.date.time)
            this.date.date = parseInt(this.value1/1000)
            console.log(this.date.date)
            this.show3 = true
        },
        Q3_method(tension_id){
            this.date.tension = tension_id
            console.log("tension"+this.date.tension)
            this.show4 =true
            if(tension_id== 0){
                     this.Q3_active1 =true
                     this.Q3_active2 =false
                     this.Q3_active3= false
                 }
                 else if (tension_id == 1){
                     this.Q3_active2 = true
                     this.Q3_active1 =false
                     this.Q3_active3 =false
                 }
                 else{
                     this.Q3_active3 = true
                     this.Q3_active2 =false
                     this.Q3_active1 =false
                 }

        },
        Q4_method(play_id){
            if(this.date.play.indexOf(play_id)== -1){
                 this.date.play.push(play_id)
                 if(play_id == 0){
                     this.Q4_active1 =true
                 }
                 else if (play_id == 1){
                     this.Q4_active2 = true
                 }
                 else{
                     this.Q4_active3 = true
                 }
            }
            else{
                var target = this.date.play.indexOf(play_id)
                this.date.play.splice(target,1)
                 if(play_id == 0){
                     this.Q4_active1 =false
                 }
                 else if (play_id == 1){
                     this.Q4_active2 = false
                 }
                 else{
                     this.Q4_active3 = false
                 }
            }
            console.log("play"+this.date.play)
            
        },
        Q5_method(budget_id){
            this.date.budget = budget_id
            console.log("budget"+this.date.budget)
            this.show6 = true
        },
        Q6_method(move_id){
            this.date.move = move_id
            console.log("move"+this.date.move)
            this.show7 = true
        },
        
        post(){
            // POST
            //this.$axios.post('http://localhost:9000',{
            this.$axios.post('http://ec2-52-194-247-32.ap-northeast-1.compute.amazonaws.com:5000/condition',{
                data:this.date,
                })
                .then(response => {
                //200 status header etc...
                 console.log(response.data)

                 this.result[0] = response.data[0]
                 this.result[1] = response.data[1]
                 this.result[2] = response.data[2]
                 
                 this.lat = this.result.Latitude
                 this.lng= this.result.Longitude
                 console.log(this.lat,this.lng)
                 this.show8 = true
                 console.log(this.result)
                })
                .catch(error => {
                 console.log(error.response)
                });
        },
    addMarker() {
      this.markers.forEach(markerInfo => {
        var contentString =
          '<div id="content">' +
          '<div id="siteNotice">' +
          "</div>" +
          '<h1 id="firstHeading" class="firstHeading">Uluru</h1>' +
          '<div id="bodyContent">' +
          "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
          "sandstone rock formation in the southern part of the " +
          "Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) " +
          "south west of the nearest large town, Alice Springs; 450&#160;km " +
          "(280&#160;mi) by road. Kata Tjuta and Uluru are the two major " +
          "features of the Uluru - Kata Tjuta National Park. Uluru is " +
          "sacred to the Pitjantjatjara and Yankunytjatjara, the " +
          "Aboriginal people of the area. It has many springs, waterholes, " +
          "rock caves and ancient paintings. Uluru is listed as a World " +
          "Heritage Site.</p>" +
          '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
          "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
          "(last visited June 22, 2009).</p>" +
          "</div>" +
          "</div>";

        // マーカー
        let marker = new google.maps.Marker({
          position: markerInfo.position,
          icon:
            "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
          map: this.map,
          // ポップなアニメーションを付与
          animation: google.maps.Animation.DROP
        });

        // マーカーのwindow
        let infowindow = new google.maps.InfoWindow({
          content: contentString
        });

        // マーカークリック時にwindow表示
        marker.addListener("click", function() {
          infowindow.open(this.map, marker);
        });
        this.formattedMarkers.push(marker);
      });
    },
    loadMap(google) {
        
        

        // googleMapを初期化
        this.map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: this.lat, lng: this.lng },
        zoom: this.zoom,
        // スワイプ判定を強めに設定(地図を移動させるには..問題)
        gestureHandling: "greedy"
        });


        this.addMarker();
    },
    release() {
      GoogleMapsLoader.release(function() {
        console.log("No google maps api around");
      });
    }
  }
};
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Kosugi+Maru');
  body{
    /*背景*/
    background-image: url("../assets/back.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    /*位置*/
    margin-left: 60px;
    margin-right: 60px;
    /*フォント*/
    font-family: 'Kosugi Maru', sans-serif;
    color: #5d5d5d;
    font-size: 20px;
  }
  .Q_title{
    margin-top: 60px;
    /*text-align: center;*/
  }
  .Q {
    position: relative;
    text-align: center;
    margin-bottom: 60px;
    }
  .Q p {
    position: absolute;
    top: 50%;
    left: 50%;
    /*-webkit-transform: translateY(-50%) translateX(-50%);*/
    transform: translateY(-90%) translateX(-50%);
    text-align: left;
    }
  .Q img {
    /*width: 100%;*/
    /*width:300px;*/
    width: 100%;
  }
  .A1 {
    position: relative;
    text-align: left;
    }
  .A1 p {
    position: absolute;
    top: 50%;
    left: 25%;
    -ms-transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    transform: translate(-50%,-50%);
    margin:0;
    padding:0;
    font-size: 16px;
    }
  .A1 img {
    width: 50%;
  }
  .A2 {
    position: relative;
    text-align: right;
    }
  .A2 p {
    position: absolute;
    top: 50%;
    left: 75%;
    -ms-transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    transform: translate(-50%,-50%);
    margin:0;
    padding:0;
    font-size: 16px;
    }
  .A2 img {
    width: 50%;
  }
  .A3 {
    position: relative;
    text-align: center;
    }
  .A3 p {
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    transform: translate(-50%,-50%);
    margin:0;
    padding:0;
    font-size: 16px;
    }
  .A3 img {
    width: 50%;
  }
  .next{
    position: relative;
    text-align: center;
    width: 20%
  }
  .send{
    text-align: center;
    margin-top: 100px;
    margin-bottom: 150px;
    font-size: 25px;
  }
  .result{
    position: relative;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-right: -80px;
    padding-left: 60px;
    padding-right: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    background-color: #f2f2f2;
    /*width:300px;*/
    /*height:100px;*/
    left: -60px;
    font-size: 15px;
  }
  .time{
    font-size: 20px;
  }
</style>
