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
          <img src="../assets/A1.svg" />
          <p> 朝 </p>
        </div>
        <div class="A2" @click="Q2_method(1)">
          <img src="../assets/A2.svg" />
          <p> 昼 </p>
        </div>
        <div class="A3" @click="Q2_method(2)">
          <img src="../assets/A3.svg" />
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
        <img src="../assets/A1.svg" />
        <p> ゆったりかなあ </p>
      </div>
      <div class="A2" @click="Q3_method(1)">
        <img src="../assets/A2.svg" />
        <p> アクティブに外出！ </p>
      </div>
      <div class="A3" @click="Q3_method(2)">
        <img src="../assets/A3.svg" />
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
          <img src="../assets/A1.svg" />
          <p> ご飯 </p>
        </div>
        <div class="A2" @click="Q4_method(1)">
          <img src="../assets/A2.svg" />
          <p> 観光 </p>
        </div>
        <div class="A3" @click="Q4_method(2)">
          <img src="../assets/A3.svg" />
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
            <img src="../assets/A1.svg" />
            <p> 節約で…（¥3,000） </p>
          </div>
          <div class="A2" @click="Q5_method(10000)">
            <img src="../assets/A2.svg" />
            <p> 普通。 （¥10,000）</p>
          </div>
          <div class="A3" @click="Q5_method(50000)">
            <img src="../assets/A3.svg" />
            <p> ☆GOYU☆（¥50,000） </p>
          </div>
        </div>
      </div>
      <!-- Q5-2 -->
        <div v-show="show6" class="transition" >
          <div> <!-- Q -->
            <img class="Q_title" src="../assets/Q5-2.svg" width="100"/>
            <div class="Q">
              <img src="../assets/Qimage.svg" />
              <p> ご飯の予算は？ </p>
            </div>
          </div>
          <div> <!-- A -->
            <div class="A1" @click="Q5_method(0)">
              <img src="../assets/A1.svg" />
              <p> チープ </p>
            </div>
            <div class="A2" @click="Q5_method(1)">
              <img src="../assets/A2.svg" />
              <p> 普通 </p>
            </div>
            <div class="A3" @click="Q5_method(2)">
              <img src="../assets/A3.svg" />
              <p> 豪華 </p>
            </div>
          </div>
        </div>
        <!-- Q7 -->
          <div v-show="show7" class="transition" >
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
       <p v-show="show9" >{{result.Name}}</p>
       <p v-show="show9" >{{result.OpeningHours}}</p>
       
</div>

</template>

<script>

    export default {
        
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
        result:{

        },
        show1:true,
        show2:false,
        show3:false,
        show4:false,
        show5:false,
        show6:false,
        show7:false,
        show8:false,
        show9:false,
        Q1_active1:false,
        Q1_active2:false,
        Q1_active3:false,
        value1: ''
        }
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
            }
            else{
                var target = this.date.time.indexOf(date_id)
                this.date.time.splice(target,1)
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
            if(this.show5 == true){

            }
        },
        Q4_method(play_id){
            if(this.date.play.indexOf(play_id)== -1){
                 this.date.play.push(play_id)
            }
            else{
                var target = this.date.play.indexOf(play_id)
                this.date.play.splice(target,1)
            }
            console.log("play"+this.date.play)
            
        },
        Q5_method(budget_id){
            this.date.budget = budget_id
            console.log("budget"+this.date.budget)
            this.show7 = true
        },
        Q6_method(move_id){
            this.date.move = move_id
            console.log("move"+this.date.move)
            this.show8 = true
        },
        
        post(){
            // POST
            this.$axios.post('http://localhost:9000',{
            //this.$axios.post('http://ec2-52-194-247-32.ap-northeast-1.compute.amazonaws.com:5000/condition',{
                data:this.date,
                })
                .then(response => {
                //200 status header etc...
                 console.log(response.data)
                 this.result = response.data
                 this.show9 = true
                 console.log(this.result)
                })
                .catch(error => {
                 console.log(error.response)
                });
        }
    }
  }
  

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
    margin-bottom: 100px;
    font-size: 25px;
  }
</style>
