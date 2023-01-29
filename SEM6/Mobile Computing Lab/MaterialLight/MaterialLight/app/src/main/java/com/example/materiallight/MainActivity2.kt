package com.example.materiallight

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        val intent = intent
        val fname = findViewById<TextView>(R.id.fname2)
        val lname = findViewById<TextView>(R.id.lname2)
        val rad2 = findViewById<TextView>(R.id.rad1)
        val cont = findViewById<TextView>(R.id.country)

        val first = intent.getStringExtra("fname")
        val last = intent.getStringExtra("lname")
        val rad = intent.getStringExtra("radio")
        val con = intent.getStringExtra("pos")

        fname.text = first
        lname.text = last
        rad2.text = rad
        cont.text = con
    }
}