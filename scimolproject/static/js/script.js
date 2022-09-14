$(function(){
    // ここにプログラムを記述
    $('#button').click(function() {
        let text_height = Number(document.getElementById('user_height').value);
        let text_weight = Number(document.getElementById('user_weight').value);
        let text_BMI = String(Math.floor(text_weight/(text_height/100)**2*100)/100);
        let text_rightweight = String(Math.floor((text_height/100)**2*22*100)/100);
        document.getElementById('user_BMI').innerHTML = text_BMI;
        document.getElementById('user_rightweight').innerHTML = text_rightweight;
    });
  });