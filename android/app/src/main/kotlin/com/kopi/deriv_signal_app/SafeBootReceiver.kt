package com.kopi.deriv_signal_app

import android.content.Context
import android.content.Intent
import android.util.Log
import id.flutter.flutter_background_service.BackgroundService
import id.flutter.flutter_background_service.BootReceiver

/**
 * The plugin's boot receiver, made safe for Android 15. When an app that was
 * force-stopped is opened again, Android re-sends BOOT_COMPLETED but refuses
 * to start a foreground service from it; the plugin does not catch that and
 * the app crashes. Here the refusal is logged, the wake lock the plugin took
 * is released, and market watch starts when the app opens instead.
 */
class SafeBootReceiver : BootReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        try {
            super.onReceive(context, intent)
        } catch (refused: IllegalStateException) {
            Log.w(TAG, "Android refused to start market watch on ${intent.action}; it starts when the app opens", refused)
            releaseWakeLock()
        }
    }

    private fun releaseWakeLock() {
        val lock = BackgroundService.lockStatic ?: return
        if (lock.isHeld) lock.release()
    }

    private companion object {
        const val TAG = "SafeBootReceiver"
    }
}
