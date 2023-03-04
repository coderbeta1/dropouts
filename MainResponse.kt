package com.example.cameraapp

import android.content.Intent
import android.graphics.Bitmap
import android.os.Bundle
import android.provider.MediaStore
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.VideoView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    private lateinit var cameraOpenId: Button
    lateinit var clickImageId: VideoView


    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        cameraOpenId = findViewById(R.id.camera_button)
        clickImageId = findViewById(R.id.videoView)

        cameraOpenId.setOnClickListener(View.OnClickListener {v: View? ->
            val cameraIntent = Intent(Mediastore.ACTION_IMAGE_CAPTURE)

            startActivityForResult(cameraIntent,pic_id)
        })
    }
}

