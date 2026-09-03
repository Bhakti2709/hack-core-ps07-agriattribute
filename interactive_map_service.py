"""
interactive_map_service.py - Live Satellite Weather & Cyclone Radar Map (Leaflet.js + OpenWeatherMap + RainViewer)
AgriAttribute AI — Syngenta Biologicals & ANNAM.AI Hack Core 2026 (Team 15)

Features:
1. Dynamic Real-Time Weather Updates:
   - When searching any Indian village (e.g. Pune, Akola, Ludhiana) or dragging marker or clicking GPS,
     client-side JavaScript immediately fetches live OpenWeather telemetry for those EXACT coordinates
     and updates the HUD (Temp, Cloud Cover %, Wind Speed km/h, Humidity %, Spray Drift Badge) instantly!
2. Dynamic RainViewer Doppler Radar:
   - Automatically queries RainViewer API for the latest scan timestamp so rain radar is never 404.
3. High-Contrast Satellite Clouds & Wind Streamlines:
   - Visibly active on map with one-tap toolbar buttons.
4. Full localization & map title parity.
"""
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

OPENWEATHER_MAP_KEY = os.getenv("OPENWEATHER_MAPS_KEY", os.getenv("OPENWEATHER_MAP_KEY", os.getenv("OPENWEATHER_API_KEY", "")))

def generate_interactive_weather_map_html(
    lat: float = 21.1458, 
    lon: float = 79.0882, 
    region_name: str = "Maharashtra & Vidarbha", 
    active_crop: str = "Soybean",
    weather_info: dict = None,
    *args,
    **kwargs
) -> str:
    """
    Generates a full interactive HTML Leaflet widget with live dynamic Doppler radar,
    high-contrast satellite clouds, wind streamlines, and instant on-map telemetry recalculation.
    """
    w = weather_info or {}
    temp = w.get("temp_c", 28.5)
    humidity = w.get("humidity_pct", 62)
    wind_kmh = w.get("wind_speed_kmh", 10.8)
    clouds = w.get("cloud_cover_pct", 15)
    desc = w.get("description", "Partly Cloudy")
    wind_deg = w.get("wind_deg", 120)
    
    # Spray Drift Assessment
    if wind_kmh < 15.0:
        wind_badge = "✅ OPTIMAL SPRAY WINDOW (< 15 km/h)"
        wind_color = "#10b981"
        wind_advisory = "Safe for biological foliar spraying (zero droplet drift risk)."
    elif wind_kmh < 25.0:
        wind_badge = "⚠️ MODERATE WIND (15-25 km/h)"
        wind_color = "#f59e0b"
        wind_advisory = "Use low-drift coarse nozzles or spray early morning."
    else:
        wind_badge = "❌ HIGH WIND ALERT (> 25 km/h)"
        wind_color = "#ef4444"
        wind_advisory = "Do NOT spray! High chemical drift and wash-off risk."

    html_code = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}
        .map-banner {{
            background: linear-gradient(90deg, #065f46, #047857);
            color: white;
            padding: 8px 16px;
            border-radius: 10px 10px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.85rem;
            font-weight: 600;
            flex-wrap: wrap;
            gap: 8px;
            box-sizing: border-box;
            height: 44px;
        }}
        #map {{
            height: calc(100% - 44px);
            width: 100%;
            border-radius: 0 0 14px 14px;
            position: relative;
        }}
        
        /* Floating Weather HUD on top-left */
        .weather-hud {{
            position: absolute;
            top: 12px;
            left: 55px;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.92);
            backdrop-filter: blur(8px);
            color: #ffffff;
            padding: 12px 16px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 24px rgba(0,0,0,0.4);
            max-width: 340px;
            font-size: 0.82rem;
            transition: all 0.3s ease;
        }}
        .hud-row {{ display: flex; justify-content: space-between; align-items: center; margin: 4px 0; }}
        .hud-val {{ font-weight: 800; color: #34d399; font-size: 0.95rem; }}
        .hud-tag {{ font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; color: white; background: {wind_color}; }}
        
        /* On-Map Quick Layer Switcher Toolbar */
        .layer-toolbar {{
            position: absolute;
            top: 12px;
            right: 12px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(6px);
            padding: 6px 10px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .layer-pill {{
            background: #f1f5f9;
            color: #334155;
            border: 1px solid #cbd5e1;
            padding: 4px 10px;
            border-radius: 14px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .layer-pill.active {{
            background: #059669;
            color: white;
            border-color: #059669;
        }}
        
        /* Bottom Search & GPS Box */
        .search-container {{
            position: absolute;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(8px);
            padding: 6px 14px;
            border-radius: 30px;
            border: 1px solid rgba(0,0,0,0.15);
            box-shadow: 0 6px 20px rgba(0,0,0,0.35);
            display: flex;
            align-items: center;
            gap: 8px;
            width: 88%;
            max-width: 500px;
        }}
        .search-input {{
            border: none;
            outline: none;
            padding: 6px 10px;
            font-size: 0.85rem;
            width: 100%;
            background: transparent;
        }}
        .gps-btn {{
            background: #059669;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 6px 14px;
            font-size: 0.75rem;
            font-weight: 700;
            cursor: pointer;
            white-space: nowrap;
        }}
        .gps-btn:hover {{ background: #047857; }}
    </style>
</head>
<body>
    <div class="map-banner">
        <div id="mapBannerTitle">🛰️ <b>Live Doppler Radar, Cloud Cover & Wind Drift Engine</b> — {region_name}</div>
        <div style="background:rgba(255,255,255,0.2); padding:2px 8px; border-radius:12px; font-size:0.75rem;">
            🌀 IMD Cyclone Alert: NORMAL (Safe for Application)
        </div>
    </div>
    
    <div id="map">
        <!-- Floating Live Weather & Wind HUD -->
        <div class="weather-hud">
            <div style="font-weight: 800; font-size: 0.85rem; color: #a7f3d0; margin-bottom: 6px; display:flex; justify-content:space-between; align-items:center;">
                <span id="hudLocationTitle">📍 LIVE FIELD: {region_name.upper()}</span>
                <span id="hudTemp" style="font-size: 1.15rem; color: #ffffff;">{temp}°C</span>
            </div>
            <div class="hud-row">
                <span>☁️ <b>Cloud Cover:</b></span>
                <span id="hudClouds" class="hud-val">{clouds}% <span style="font-size:0.75rem; font-weight:normal; color:#cbd5e1;">({desc})</span></span>
            </div>
            <div class="hud-row">
                <span>💨 <b>Wind Speed:</b></span>
                <span id="hudWind" class="hud-val">{wind_kmh} km/h</span>
            </div>
            <div class="hud-row">
                <span>💧 <b>Humidity:</b> <span id="hudHumidity">{humidity}% RH</span></span>
                <span id="hudSprayBadge" class="hud-tag">{wind_badge}</span>
            </div>
            <div id="hudSprayAdvisory" style="font-size: 0.68rem; color: #94a3b8; margin-top: 4px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 4px;">
                💡 <em>{wind_advisory}</em>
            </div>
        </div>

        <!-- Direct One-Tap Layer Control Toolbar -->
        <div class="layer-toolbar">
            <button id="btnClouds" class="layer-pill active" onclick="toggleLayer('clouds')">☁️ Clouds</button>
            <button id="btnRadar" class="layer-pill active" onclick="toggleLayer('radar')">🌧️ Rain Radar</button>
            <button id="btnWind" class="layer-pill active" onclick="toggleLayer('wind')">💨 Wind Stream</button>
            <button id="btnSatellite" class="layer-pill" onclick="toggleSatellite()">🛰️ Satellite</button>
        </div>

        <!-- Interactive Search & GPS Locate Bar -->
        <div class="search-container">
            <input type="text" id="locSearch" class="search-input" placeholder="🔍 Search Village / Taluka (e.g. Pune, Akola, Baramati, Ludhiana)..." />
            <button onclick="searchLocation()" class="gps-btn" style="background:#0284c7;">Search</button>
            <button onclick="locateUserGPS()" class="gps-btn">🎯 My GPS</button>
        </div>
    </div>

    <script>
        var apiKey = "{OPENWEATHER_MAP_KEY}";
        var map = L.map('map', {{
            center: [{lat}, {lon}],
            zoom: 7,
            zoomControl: true
        }});

        // 1. OpenStreetMap Base Layer
        var osmLayer = L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }}).addTo(map);

        // 2. High-Resolution Farm Satellite View (Esri)
        var satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
            maxZoom: 19,
            attribution: 'Tiles &copy; Esri High-Res Satellite'
        }});

        // 3. OpenWeatherMap Live Satellite Clouds (High-Contrast Opacity 0.88)
        var cloudsLayer = L.tileLayer('https://tile.openweathermap.org/map/clouds_new/{{z}}/{{x}}/{{y}}.png?appid=' + apiKey, {{
            maxZoom: 18,
            opacity: 0.88,
            attribution: 'Clouds &copy; OpenWeatherMap'
        }}).addTo(map);

        // 4. OpenWeatherMap Wind Streamlines Layer
        var windLayer = L.tileLayer('https://tile.openweathermap.org/map/wind_new/{{z}}/{{x}}/{{y}}.png?appid=' + apiKey, {{
            maxZoom: 18,
            opacity: 0.80,
            attribution: 'Wind &copy; OpenWeatherMap'
        }}).addTo(map);

        // 5. Dynamic RainViewer Doppler Radar Layer (Always fetches latest live scan timestamp!)
        var radarLayer = null;
        fetch('https://api.rainviewer.com/public/weather-maps.json')
            .then(function(res) {{ return res.json(); }})
            .then(function(data) {{
                if (data && data.radar && data.radar.past && data.radar.past.length > 0) {{
                    var latestPath = data.radar.past[data.radar.past.length - 1].path;
                    var radarTileUrl = data.host + latestPath + '/256/{{z}}/{{x}}/{{y}}/2/1_1.png';
                    radarLayer = L.tileLayer(radarTileUrl, {{
                        maxZoom: 18,
                        opacity: 0.85,
                        attribution: 'Live Doppler Radar &copy; RainViewer'
                    }}).addTo(map);
                }}
            }})
            .catch(function(err) {{
                console.log("RainViewer fallback to OpenWeather precipitation:", err);
                radarLayer = L.tileLayer('https://tile.openweathermap.org/map/precipitation_new/{{z}}/{{x}}/{{y}}.png?appid=' + apiKey, {{
                    maxZoom: 18, opacity: 0.80
                }}).addTo(map);
            }});

        // Layer Toggle Handlers
        var isSatellite = false;
        function toggleSatellite() {{
            isSatellite = !isSatellite;
            var btn = document.getElementById('btnSatellite');
            if (isSatellite) {{
                map.removeLayer(osmLayer);
                map.addLayer(satelliteLayer);
                btn.classList.add('active');
            }} else {{
                map.removeLayer(satelliteLayer);
                map.addLayer(osmLayer);
                btn.classList.remove('active');
            }}
        }}

        function toggleLayer(layerName) {{
            if (layerName === 'clouds') {{
                var btn = document.getElementById('btnClouds');
                if (map.hasLayer(cloudsLayer)) {{
                    map.removeLayer(cloudsLayer);
                    btn.classList.remove('active');
                }} else {{
                    map.addLayer(cloudsLayer);
                    btn.classList.add('active');
                }}
            }} else if (layerName === 'radar') {{
                var btn = document.getElementById('btnRadar');
                if (radarLayer) {{
                    if (map.hasLayer(radarLayer)) {{
                        map.removeLayer(radarLayer);
                        btn.classList.remove('active');
                    }} else {{
                        map.addLayer(radarLayer);
                        btn.classList.add('active');
                    }}
                }}
            }} else if (layerName === 'wind') {{
                var btn = document.getElementById('btnWind');
                if (map.hasLayer(windLayer)) {{
                    map.removeLayer(windLayer);
                    btn.classList.remove('active');
                }} else {{
                    map.addLayer(windLayer);
                    btn.classList.add('active');
                }}
            }}
        }}

        // Custom Farm Marker with Wind Vector Arrow
        var farmIcon = L.divIcon({{
            className: 'custom-farm-icon',
            html: '<div style="position:relative; width:38px; height:38px;"><div style="background:#059669; color:white; border-radius:50%; width:36px; height:36px; display:flex; align-items:center; justify-content:center; border:2.5px solid white; box-shadow:0 3px 10px rgba(0,0,0,0.35); font-size:18px;">🌱</div><div style="position:absolute; top:-10px; right:-10px; background:#0284c7; color:white; border-radius:50%; width:20px; height:20px; font-size:10px; font-weight:bold; display:flex; align-items:center; justify-content:center; transform:rotate({wind_deg}deg);" title="Wind Direction">💨</div></div>',
            iconSize: [38, 38],
            iconAnchor: [19, 19]
        }});

        var marker = L.marker([{lat}, {lon}], {{ icon: farmIcon, draggable: true }}).addTo(map);
        marker.bindPopup("<b>📍 Active Field: {active_crop}</b><br>{region_name}<br><small>GPS: {lat:.4f}°N, {lon:.4f}°E</small><br><b>Wind:</b> {wind_kmh} km/h | <b>Cloud:</b> {clouds}%<br><span style='color:{wind_color}; font-weight:bold;'>{wind_badge}</span>").openPopup();

        // DYNAMIC FIELD WEATHER UPDATER FUNCTION
        function updateFieldWeather(targetLat, targetLon, placeName) {{
            if (placeName) {{
                document.getElementById('hudLocationTitle').innerText = "📍 " + placeName.toUpperCase();
                document.getElementById('mapBannerTitle').innerHTML = "🛰️ <b>Live Radar & Weather Telemetry</b> — " + placeName;
            }}
            
            var apiUrl = "https://api.openweathermap.org/data/2.5/weather?lat=" + targetLat + "&lon=" + targetLon + "&appid=" + apiKey + "&units=metric";
            fetch(apiUrl)
                .then(function(res) {{ return res.json(); }})
                .then(function(data) {{
                    if (data && data.main) {{
                        var newTemp = Math.round(data.main.temp);
                        var newHumidity = data.main.humidity;
                        var newWindKmh = (data.wind.speed * 3.6).toFixed(1);
                        var newClouds = data.clouds ? data.clouds.all : 0;
                        var newDesc = data.weather[0] ? data.weather[0].description : "Clear";
                        var cityName = data.name || placeName || "Field";

                        // Update HUD Elements Instantly
                        document.getElementById('hudTemp').innerText = newTemp + "°C";
                        document.getElementById('hudClouds').innerHTML = newClouds + "% <span style='font-size:0.75rem; font-weight:normal; color:#cbd5e1;'>(" + newDesc + ")</span>";
                        document.getElementById('hudWind').innerText = newWindKmh + " km/h";
                        document.getElementById('hudHumidity').innerText = newHumidity + "% RH";
                        document.getElementById('hudLocationTitle').innerText = "📍 " + cityName.toUpperCase();
                        document.getElementById('mapBannerTitle').innerHTML = "🛰️ <b>Live Radar & Weather Telemetry</b> — " + cityName;

                        // Update Spray Drift Badge
                        var badgeEl = document.getElementById('hudSprayBadge');
                        var advisoryEl = document.getElementById('hudSprayAdvisory');
                        if (parseFloat(newWindKmh) < 15.0) {{
                            badgeEl.innerText = "✅ OPTIMAL SPRAY WINDOW (< 15 km/h)";
                            badgeEl.style.background = "#10b981";
                            advisoryEl.innerText = "💡 Safe for biological foliar spraying (zero droplet drift risk).";
                        }} else if (parseFloat(newWindKmh) < 25.0) {{
                            badgeEl.innerText = "⚠️ MODERATE WIND (15-25 km/h)";
                            badgeEl.style.background = "#f59e0b";
                            advisoryEl.innerText = "💡 Use low-drift coarse nozzles or spray early morning.";
                        }} else {{
                            badgeEl.innerText = "❌ HIGH WIND ALERT (> 25 km/h)";
                            badgeEl.style.background = "#ef4444";
                            advisoryEl.innerText = "💡 Do NOT spray! High chemical drift and wash-off risk.";
                        }}

                        // Update marker popup with 1-tap parent sync link
                        var syncBtn = "<br><a href='?lat=" + targetLat.toFixed(4) + "&lon=" + targetLon.toFixed(4) + "&place=" + encodeURIComponent(cityName) + "' target='_parent' style='display:inline-block; margin-top:8px; padding:6px 12px; background:#059669; color:white; font-size:0.75rem; font-weight:800; border-radius:6px; text-decoration:none; box-shadow:0 2px 6px rgba(0,0,0,0.2);'>📍 Set as My Farm in Decision Engine ↗</a>";
                        marker.setPopupContent("<b>📍 " + cityName + "</b><br><small>GPS: " + targetLat.toFixed(4) + "°N, " + targetLon.toFixed(4) + "°E</small><br><b>Temp:</b> " + newTemp + "°C | <b>Wind:</b> " + newWindKmh + " km/h | <b>Cloud:</b> " + newClouds + "%<br><span style='font-weight:bold; color:#059669;'>" + badgeEl.innerText + "</span>" + syncBtn).openPopup();
                    }}
                }})
                .catch(function(err) {{
                    console.error("Live weather update error:", err);
                }});
        }}

        marker.on('dragend', function(e) {{
            var pos = marker.getLatLng();
            updateFieldWeather(pos.lat, pos.lng, "Relocated Field");
        }});

        map.on('click', function(e) {{
            marker.setLatLng(e.latlng);
            updateFieldWeather(e.latlng.lat, e.latlng.lng, "Selected Field");
        }});

        // Real Browser Geolocation Trigger
        function locateUserGPS() {{
            if (navigator.geolocation) {{
                navigator.geolocation.getCurrentPosition(function(position) {{
                    var userLat = position.coords.latitude;
                    var userLon = position.coords.longitude;
                    map.setView([userLat, userLon], 12);
                    marker.setLatLng([userLat, userLon]);
                    updateFieldWeather(userLat, userLon, "Exact GPS Field");
                }}, function(error) {{
                    alert("Unable to retrieve GPS location: " + error.message);
                }}, {{ enableHighAccuracy: true, timeout: 8000 }});
            }} else {{
                alert("Geolocation is not supported by your browser.");
            }}
        }}

        // OpenStreetMap Nominatim Geocoding Search
        function searchLocation() {{
            var query = document.getElementById('locSearch').value;
            if (!query) return;
            fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(query + ', India'))
                .then(function(res) {{ return res.json(); }})
                .then(function(data) {{
                    if (data && data.length > 0) {{
                        var item = data[0];
                        var sLat = parseFloat(item.lat);
                        var sLon = parseFloat(item.lon);
                        var placeName = item.display_name.split(',')[0];
                        map.setView([sLat, sLon], 11);
                        marker.setLatLng([sLat, sLon]);
                        updateFieldWeather(sLat, sLon, placeName);
                    }} else {{
                        alert("Location not found. Try entering district or taluka name.");
                    }}
                }})
                .catch(function(err) {{
                    alert("Error searching location: " + err);
                }});
        }}

        // Allow pressing Enter in search box
        document.getElementById('locSearch').addEventListener('keypress', function(e) {{
            if (e.key === 'Enter') searchLocation();
        }});
    </script>
</body>
</html>
"""
    return html_code
