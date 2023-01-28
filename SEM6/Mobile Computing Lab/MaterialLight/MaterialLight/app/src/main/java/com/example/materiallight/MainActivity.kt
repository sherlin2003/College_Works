package com.example.materiallight

import android.content.Intent
import android.os.Bundle
import android.text.Html
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import android.widget.ArrayAdapter

class MainActivity : AppCompatActivity(){
    private lateinit var radioGroup: RadioGroup
    lateinit var Spinner: Spinner
    var pos = 0
    var str : String = " "
    // on below line we are creating a variable for our list of data to be displayed in spinner.
    var Country =
        arrayOf<String>("India","Pakistan","China","Korea")
    private lateinit var selectedRadioButton: RadioButton
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        supportActionBar?.title = Html.fromHtml("<font color=\"black\">" + getString(R.string.app_name) + "</font>");
        val btn = findViewById<Button>(R.id.contin)
        val fname = findViewById<TextView>(R.id.fname1)
        val lname = findViewById<TextView>(R.id.lname1)

        radioGroup = findViewById(R.id.radioGroup)
        Spinner = findViewById(R.id.spinner)


        // on below line we are initializing adapter for our spinner
        val adapter: ArrayAdapter<CharSequence> =
            ArrayAdapter(this, android.R.layout.simple_spinner_item, Country)

        // on below line we are setting drop down view resource for our adapter.
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        // on below line we are setting adapter for spinner.
        Spinner.adapter = adapter

        // on below line we are creating a variable to which we have to set our spinner item selected.
        val selection = "India"

        // on below line we are getting the position of the item by the item name in our adapter.
        val spinnerPosition: Int = adapter.getPosition(selection)

        // on below line we are setting selection for our spinner to spinner position.
        Spinner.setSelection(spinnerPosition)

        Spinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(p0: AdapterView<*>?, p1: View?, p2: Int, p3: Long) {

                Toast.makeText(applicationContext, Country[p2], Toast.LENGTH_SHORT).show()
                str = Country[p2]
            }
            override fun onNothingSelected(p0: AdapterView<*>?) {
            }
        }

        btn.setOnClickListener {
            if(!fname.text.toString().isNullOrEmpty() && !lname.text.toString().isNullOrEmpty()) {
                val intent = Intent(this, MainActivity2::class.java)
                intent.putExtra("fname", fname.text.toString())
                intent.putExtra("lname", lname.text.toString())
                val selectedRadioButtonId: Int = radioGroup.checkedRadioButtonId

                if (selectedRadioButtonId != -1) {
                    selectedRadioButton = findViewById(selectedRadioButtonId)
                    val string: String = selectedRadioButton.text.toString()
                    intent.putExtra("radio", string)
                    intent.putExtra("pos", str)
                }
                startActivity(intent)

            }
            else
            {
                Toast.makeText(applicationContext,"Enter the required fields", Toast.LENGTH_SHORT).show()
            }
        }
    }
}


