import 'dart:convert';

import 'package:flutter/services.dart';

import '../domain/playbook.dart';

Future<Playbook> loadPlaybook() async => Playbook.fromJson(
    jsonDecode(await rootBundle.loadString('assets/strategies.json')) as Map<String, dynamic>);
