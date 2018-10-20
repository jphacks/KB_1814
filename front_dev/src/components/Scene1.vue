<template>
<div>
    <el-button @click="show2 = !show2">Start</el-button>
    <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
    <p>場所指定してね{{date.region}}</p>
      <transition name="el-zoom-in-center" >
        <el-button v-show="show2"  class="transition-box" @click="Q1_method(0)" >京都</el-button>

      </transition>

      <transition name="el-zoom-in-top">
        <el-button v-show="show2" class="transition-box" @click="Q1_method(1)" >大阪</el-button>
      </transition>

      <transition name="el-zoom-in-bottom">
        <el-button  v-show="show2" class="transition-box" @click="Q1_method(2)">神戸</el-button >
      </transition>
    </div>

    <div class="block" v-show="show3" style="display: flex; margin-top: 50px; height: 100px;margin-left : 350px">
    <span class="demonstration">DateTime </span><br>
    <el-date-picker
      v-model="value4"
      type="datetimerange"
      range-separator="To"
      start-placeholder="Start date"
      end-placeholder="End date">
    </el-date-picker>
    
  </div>

  <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
      <transition name="el-zoom-in-center">
        <el-button v-show="show3" class="transition-box" @click="Q3_method(0)">まったり〜</el-button>
      </transition>

      <transition name="el-zoom-in-top">
        <div v-show="show3" class="transition-box" @click="Q3_method(1)">アクティブ（インドア）</div>
      </transition>

      <transition name="el-zoom-in-bottom">
        <div v-show="show3" class="transition-box" @click="Q3_method(2)">アクティブ（アウトドア）</div>
      </transition>
    </div>

    <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
      <transition name="el-zoom-in-center">
        <el-button v-show="show4" class="transition-box" @click="Q4_method(0)">観光</el-button>
      </transition>

      <transition name="el-zoom-in-top">
        <div v-show="show4" class="transition-box" @click="Q4_method(1)">ご飯andカフェ</div>
      </transition>

      <transition name="el-zoom-in-bottom">
        <div v-show="show4" class="transition-box" @click="Q4_method(2)">スポーツ</div>
      </transition>
    </div>

    <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
      <transition name="el-zoom-in-center">
        <el-button v-show="show5" class="transition-box" @click="Q5_method(0)">3000円</el-button>
      </transition>

      <transition name="el-zoom-in-top">
        <div v-show="show5" class="transition-box" @click="Q5_method(1)">5000円</div>
      </transition>

      <transition name="el-zoom-in-bottom">
        <div v-show="show5" class="transition-box" @click="Q5_method(2)">1万円</div>
      </transition>
    </div>

    <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
      <transition name="el-zoom-in-center">
        <el-button v-show="show6" class="transition-box" @@click="Q6_method(0)">車</el-button>
      </transition>

      <transition name="el-zoom-in-top">
        <div v-show="show6" class="transition-box" @click="Q6_method(1)">徒歩</div>
      </transition>

      <transition name="el-zoom-in-bottom">
        <div v-show="show6" class="transition-box" @click="Q6_method(2)">電車</div>
      </transition>
    </div>

    <div style="display: flex; margin-top: 20px; height: 100px;margin-left : 350px">
    <el-button v-show="show7" class="transition-box" @click="post">送信</el-button>
    </div>
  </div>
</template>

<script>

    export default {
        
    data(){
      return{
        date:{
                region:[],
                date_start:null,
                date_end:null,
                tension:null,
                play:null,
                budget:null,
                move:null,
        },
        show2:false,
        show3:false,
        show4:false,
        show5:false,
        show6:false,
        show7:true,
        show8:true,
        value4: [new Date(2018, 10, 10, 10, 10), new Date(2018, 10, 11, 10, 10)]
        }
    },
    methods:{
        Q1_method(region_id){
            if(this.date.region.indexOf(region_id)==0){
                 this.date.region.push(region_id)
            }
            else{
                this.date.region.some(function(v, i){
                if (v==region_id) this.data.region.splice(i,1);    
            });

            }
            console.log("region"+this.date.region)
            this.show3 =true
        },
        Q3_method(tension_id){
            this.date.tension = tension_id
            console.log("tension"+this.date.tension)
            this.show4 =true
            if(this.show5 == true){

            }
        },
        Q4_method(play_id){
            this.date.play = play_id
            console.log("play"+this.date.play)
            this.show5=true
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
        datetime(){
            this.date.date_start = parseInt(this.value4[0]/1000)
            this.date.date_end = parseInt(this.value4[1]/1000)
            console.log(this.date.date_start)
        },

        post(){
            // POST
            this.$axios.post('http://ec2-52-194-247-32.ap-northeast-1.compute.amazonaws.com:5000/condition',{
                data:this.date,
                
                })
                .then(response => {
                //200 status header etc...
                 console.log(response)
                })
                .catch(error => {
                 console.log(error.response)
                });
        }
    }
  }

</script>

<style>
  .transition-box {
    margin-bottom: 10px;
    width: 200px;
    height: 100px;
    border-radius: 4px;
    background-color: #409EFF;
    text-align: center;
    color: #fff;
    padding: 40px 20px;
    box-sizing: border-box;
    margin-right: 20px;
  }
</style>
