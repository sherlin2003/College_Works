package com.example.feedbackform

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.RatingBar
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?)
    {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val rat = findViewById<RatingBar>(R.id.ratingBar)
        val button = findViewById<Button>(R.id.button)
        val txt = findViewById<TextView>(R.id.editTextTextPersonName)
        val fd = findViewById<TextView>(R.id.textView2)
        rat.setOnRatingBarChangeListener { ratingBar, fl, b ->
            val rate = fl.toInt()
            if(rate==5)
                txt.text="Awesome. I love it"
            else if(rate==4)
                txt.text="Good. Enjoyed it"
            else if(rate==3)
                txt.text="Satisfied"
            else if(rate==2)
                txt.text="Not good. Need improvement"
            else if(rate==1)
                txt.text="Disappointed. Very poor"
            else
                txt.text=" "
            button.setOnClickListener {
                txt.text = " "
                Toast.makeText(applicationContext,"Feedback is successfully submitted",Toast.LENGTH_SHORT).show()
                fd.text=" "
                rat.rating= 0F
            }
        }
    }
}
