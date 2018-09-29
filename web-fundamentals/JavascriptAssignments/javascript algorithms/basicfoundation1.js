function printto255(){
    var arr = [];
    for (var i = 1; i < 256; i++){
        arr.push(i);
    }
    return arr;
}


function sum_even_1000(){
    var sum = 0;
    for (var i = 1; i < 1001; i++){
        if(i % 2 === 0){
            sum+=i 
        }
    }
    return sum;
}


function sum_odd_5000(){
    var sum = 0;
    for (var i = 1; i < 5000; i++){
        if(i % 2 === 1){
            sum+=i
        }
    }
    return sum;
}


function iterate(arr){
    var sum = 0;
    for (var i = 0; i < arr.length; i++){
        sum+=arr[i];
    }
    return sum;
}


function findMax(arr){
    var max = arr[0];
    for (var i = 1; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}


function findAvg(arr){
    var sum = 0;
    for (var i = 0; i < arr.length; i++){
        sum+=arr[i];
    }
    return sum/arr.length;
}


function arrayOdd(){
    var arr = [];
    for (var i = 1; i < 50; i++){
        if(i % 2 === 1){
            arr.push(i);
        }
    }
    return arr;
}


function greaterthanY(arr, Y){
    var count = 0;
    for (var i = 0; i < arr.length; i++){
        if(arr[i] > Y){
            count++;
        }
    }
    return count;
}


function Squares(arr){
    for (var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * arr[i];
    }
    return arr;
}


function Negatives(arr){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}


function MaxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];

    for (var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
        sum+=arr[i];
    }
    var avg = sum/arr.length;
    var arrnew = (max, min, avg);
    return arrnew;
}


function swapVals(arr){
    var temp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;
    return arr;
}


function numtoString(arr){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 'Dojo';
        }
    }
    return arr;
}