---
name: Lumina Velocity
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#bccac3'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#86948e'
  outline-variant: '#3d4945'
  surface-tint: '#66daba'
  primary: '#66daba'
  on-primary: '#00382c'
  primary-container: '#21a385'
  on-primary-container: '#003025'
  inverse-primary: '#006b56'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#ffb4a6'
  on-tertiary: '#5e170c'
  tertiary-container: '#d97462'
  on-tertiary-container: '#541006'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#84f7d5'
  primary-fixed-dim: '#66daba'
  on-primary-fixed: '#002018'
  on-primary-fixed-variant: '#005140'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a6'
  on-tertiary-fixed: '#3f0300'
  on-tertiary-fixed-variant: '#7c2d20'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  signature-gradient: 'linear-gradient(90deg, #A855F7 0%, #EC4899 33%, #F97316 66%,
    #EAB308 100%)'
  map-void: '#020617'
  glass-border: rgba(255, 255, 255, 0.12)
  warning-amber: '#F59E0B'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 24px
  gutter: 16px
  touch-target: 44px
---

## Brand & Style

The design system for ParkBy is defined by a high-tech, premium aesthetic that blends **Glassmorphism** with a **Dark Mode** foundation. It is designed to feel like a high-end automotive interface—precise, futuristic, and efficient. The target audience includes urban commuters and tech-savvy travelers who value speed and reliability. 

The visual narrative relies on depth and translucency. Surfaces are treated as "optical glass" layered over a dynamic map environment. The experience should evoke a sense of calm control amidst the chaos of urban navigation. High-contrast interactions ensure the system remains functional in high-glare environments, such as a phone mounted on a dashboard.

## Colors

The palette is optimized for a **Dark Mode** primary experience to reduce eye strain and emphasize the map-centric nature of the application. 

- **Primary Teal-Green:** Used strictly for actionable intelligence—CTAs, active map pins, and successful states.
- **Signature Gradient:** This is the "high-energy" accent. It should be used sparingly for premium features, onboarding highlights, or "instant-book" urgency.
- **Neutral Backgrounds:** We use a deep "Map Void" (#020617) for the lowest layer, with "Slate Navy" (#0F172A) for containers to maintain depth without pure black crushing.
- **Accessibility:** All text-on-background combinations must maintain a 4.5:1 ratio. Interactive elements on the map must have a 2px high-contrast stroke to ensure visibility against varying map textures.

## Typography

This system employs a tri-font strategy to differentiate intent:
1. **Space Grotesk (Headlines):** Its geometric, slightly eccentric terminals lend a "tech-forward" feel to page titles and large headers.
2. **Inter (Interface/Body):** Used for all functional UI text, descriptions, and settings. It provides maximum legibility and a neutral tone.
3. **JetBrains Mono (Numerical/Data):** Monospaced characters ensure that prices, time durations, and parking zone codes are perfectly aligned and easy to scan at a glance.

**Hierarchy Note:** Use `data-lg` for pricing inside buttons or map callouts. Use `label-caps` for small meta-tags like "AVAILABLE" or "RESERVED".

## Layout & Spacing

The layout is built on an **8px base grid**. We utilize a **Fluid Grid** system that expands to 12 columns on desktop but maintains a strict 24px side margin on mobile.

- **Mobile First:** Navigation and search are anchored to the bottom of the screen for thumb-friendly interaction.
- **Vertical Rhythm:** Components are separated by increments of 8px (16, 24, 32).
- **Safe Zones:** Ensure a 44px minimum tap target for all interactive elements, particularly map filters and pin clusters, to accommodate users who may be interacting with the device while in a vehicle.

## Elevation & Depth

Depth is the primary communicator of hierarchy. We do not use solid shadows; instead, we use **Tonal Glassmorphism**:

1. **Background:** A vignetted, dark map texture with a subtle blur overlay.
2. **Level 1 (Panels):** `background: rgba(15, 23, 42, 0.7)`, `backdrop-filter: blur(12px)`, `border: 1px solid rgba(255, 255, 255, 0.08)`.
3. **Level 2 (Modals/Popovers):** `background: rgba(30, 41, 59, 0.8)`, `backdrop-filter: blur(20px)`, `border: 1px solid rgba(255, 255, 255, 0.15)`.
4. **Shadows:** Use a "Glow Shadow" for active elements: `0 24px 48px -12px rgba(0, 0, 0, 0.5)`. For the Signature Gradient elements, use a colored drop shadow that matches the gradient's mid-tone.

## Shapes

The shape language is **Rounded (Level 2)**. This strikes a balance between the precision of a technical tool and the approachability of a consumer app.

- **Standard Elements:** 0.5rem (8px) radius for input fields and small cards.
- **Large Containers:** 1rem (16px) for bottom sheets and main dashboard panels.
- **Interactive Pill:** Map filters and "Instant Book" buttons use a full pill radius to differentiate them from static content.

## Components

- **Primary Buttons:** Solid Teal-Green (#0F9B7E) with white text. Use JetBrains Mono for the price within the button (e.g., "Book for $12.00").
- **Glass Cards:** Used for parking spot listings. They feature the 1px translucent border and frosted blur. Background color should shift slightly lighter on hover.
- **Input Fields:** Dark, semi-transparent backgrounds with a 1px border. On focus, the border transitions to a Teal-Green glow or a Signature Gradient border for high-priority search.
- **Map Pins:** Custom teardrop shapes. Active pins use the Teal-Green; "Premium" or "Suggested" pins use the Signature Gradient.
- **Chips/Filters:** Pill-shaped with a glass background. Active state uses a solid white or teal background with dark text to provide maximum contrast.
- **Focus Rings:** For accessibility, all focused elements must display a 2px offset ring in Teal-Green or High-Contrast White.