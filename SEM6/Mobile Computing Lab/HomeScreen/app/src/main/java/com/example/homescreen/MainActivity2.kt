package com.example.homescreen
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.annotation.SuppressLint
import android.view.View

class MainActivity2 : AppCompatActivity() {
    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val button1 = findViewById<Button>(R.id.button4)
        val button2 = findViewById<Button>(R.id.button2)

        button1.setOnClickListener() {
            button1.visibility = View.VISIBLE
            val abc = Intent(this@MainActivity2, MainActivity3::class.java)
            startActivity(abc)
        }
        button2.setOnClickListener()
        {
            button2.visibility = View.VISIBLE
            val abc = Intent(this@MainActivity2, MainActivity::class.java)
            //abc.putExtra("fname", finame)
            startActivity(abc)
        }
    }
}


//        val intent = intent
//        val fname = findViewById<TextView>(R.id.fname)
//        val lname = findViewById<TextView>(R.id.lname)
//        val phone = findViewById<TextView>(R.id.phonenumber)
//        val email = findViewById<TextView>(R.id.mail)
//        val bday = findViewById<TextView>(R.id.birthdate)
//        val gender = findViewById<TextView>(R.id.gender)
//        val address = findViewById<TextView>(R.id.address)
//        val Confirm = findViewById<Button>(R.id.button4)
//        val Edit = findViewById<Button>(R.id.button2)
//
//        val first = intent.getStringExtra("fname")
//        val last = intent.getStringExtra("lname")
//        val phonenumber = intent.getStringExtra("phone")
//        val mail = intent.getStringExtra("mailid")
//        val date = intent.getStringExtra("date")
//        val gen = intent.getStringExtra("gen")
//        val add = intent.getStringExtra("add")
//
//        fname.text = first
//        lname.text = last
//        phone.text= phonenumber
//        email.text= mail
//        bday.text= date
//        gender.text= gen
//        address.text= add
//
//        Confirm.setOnClickListener {
//            val intent = Intent(this@MainActivity2, MainActivity3::class.java)
//            startActivity(intent)
//        }
//        Edit.setOnClickListener {
//            val intent = Intent(this@MainActivity2, MainActivity::class.java)
//            startActivity(intent)
//        }
