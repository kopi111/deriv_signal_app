import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../domain/setup_check.dart';

/// Petrol-teal instrument panel. Buy is sea green, sell is coral, waiting is sand.
class DeskColors {
  static const petrol = Color(0xFF0F2B33);
  static const surface = Color(0xFF16363F);
  static const raised = Color(0xFF1E4750);
  static const line = Color(0xFF2D5A63);
  static const ink = Color(0xFFE9F0EC);
  static const muted = Color(0xFF9DB7B4);
  static const buy = Color(0xFF3CC49A);
  static const sell = Color(0xFFF2735F);
  static const waiting = Color(0xFFD2B77E);

  static Color of(TradeDirection direction) =>
      direction == TradeDirection.buy ? buy : sell;
}

class DeskType {
  static TextStyle display(double size, {Color color = DeskColors.ink}) =>
      GoogleFonts.barlowCondensed(
        fontSize: size,
        fontWeight: FontWeight.w600,
        color: color,
        height: 1.0,
        fontFeatures: const [FontFeature.tabularFigures()],
      );

  static TextStyle figure(double size, {Color color = DeskColors.ink}) =>
      GoogleFonts.barlowCondensed(
        fontSize: size,
        fontWeight: FontWeight.w500,
        color: color,
        fontFeatures: const [FontFeature.tabularFigures()],
      );

  static TextStyle body(double size, {Color color = DeskColors.ink, FontWeight weight = FontWeight.w400}) =>
      GoogleFonts.barlow(fontSize: size, color: color, fontWeight: weight, height: 1.35);
}

ThemeData buildDeskTheme() {
  final base = ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,
    scaffoldBackgroundColor: DeskColors.petrol,
    colorScheme: const ColorScheme.dark(
      surface: DeskColors.surface,
      primary: DeskColors.buy,
      secondary: DeskColors.waiting,
      error: DeskColors.sell,
      onSurface: DeskColors.ink,
    ),
  );
  return base.copyWith(
    textTheme: GoogleFonts.barlowTextTheme(base.textTheme).apply(
      bodyColor: DeskColors.ink,
      displayColor: DeskColors.ink,
    ),
    dividerColor: DeskColors.line,
    navigationBarTheme: NavigationBarThemeData(
      backgroundColor: DeskColors.surface,
      indicatorColor: DeskColors.raised,
      labelTextStyle: WidgetStatePropertyAll(DeskType.body(13, color: DeskColors.muted)),
    ),
    inputDecorationTheme: const InputDecorationTheme(
      border: OutlineInputBorder(borderSide: BorderSide(color: DeskColors.line)),
      enabledBorder: OutlineInputBorder(borderSide: BorderSide(color: DeskColors.line)),
      isDense: true,
    ),
  );
}
