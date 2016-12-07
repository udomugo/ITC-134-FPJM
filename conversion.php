<?php

 function c_to_f($temp)
    {
        $fahrenheit=$temp * 9/5 + 32;
        return $fahrenheit ;
    }

    function f_to_c($temp)
    {
        $celsius= 5/9 * ($temp-32);
        return $celsius ;
    }

?>