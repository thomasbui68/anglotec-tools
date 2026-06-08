import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router';
import CountUp from 'react-countup';
import {
  Shield,
  Brain,
  GraduationCap,
  Globe,
  Gift,
  TrendingUp,
  CheckCircle,
  ArrowRight,
  Calculator,
  Mic,
  Stethoscope,
  Sparkles,
  Quote,
  Calendar,
  Users,
  Award,
  MapPin,
} from 'lucide-react';
import Layout from '@/components/Layout';

/* ─────────────────── Scroll Reveal Hook ─────────────────── */
function useScrollReveal(threshold = 0.15) {
  const ref = useRef<any>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.unobserve(el);
        }
      },
      { threshold }
    );
    observer.observe(el);
    return () => observer.disconnect();
  }, [threshold]);

  return { ref, visible };
}

/* ─────────────────── Particle Field ─────────────────── */
function ParticleField() {
  const particles = Array.from({ length: 35 }, (_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    size: 2 + Math.random() * 2,
    duration: 15 + Math.random() * 10,
    delay: Math.random() * 15,
    opacity: 0.15 + Math.random() * 0.15,
  }));

  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      {particles.map((p) => (
        <div
          key={p.id}
          className="absolute rounded-full bg-sage-green animate-float-up"
          style={{
            left: p.left,
            bottom: '-10px',
            width: `${p.size}px`,
            height: `${p.size}px`,
            opacity: p.opacity,
            animationDuration: `${p.duration}s`,
            animationDelay: `${p.delay}s`,
          }}
        />
      ))}
    </div>
  );
}

/* ─────────────────── Section 1: Hero ─────────────────── */
function HeroSection() {
  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section className="relative min-h-[100dvh] overflow-hidden flex items-center">
      {/* Real campus photo background */}
      <div
        className="absolute inset-0"
        style={{ backgroundImage: 'url(/campus-hero.jpg)', backgroundSize: 'cover', backgroundPosition: 'center' }}
      />
      {/* Dark overlay for text readability */}
      <div className="absolute inset-0 bg-gradient-to-r from-[#1a2f28]/95 via-[#1a2f28]/80 to-[#1a2f28]/60" />
      <div className="absolute inset-0 bg-gradient-to-t from-[#1a2f28]/50 to-transparent" />
      <ParticleField />

      <div className="container-main relative z-10 pt-[72px] pb-20">
        <div className="max-w-3xl">
          {/* Overline */}
          <p
            className="text-caption text-muted-olive mb-6"
            style={{
              opacity: 0,
              animation: 'fade-in-up 0.4s cubic-bezier(0.16,1,0.3,1) 0.2s forwards',
            }}
          >
            British Council Accredited Since 1986
          </p>

          {/* Headline */}
          <h1
            className="text-display font-heading text-white mb-6"
            style={{
              opacity: 0,
              animation: 'fade-in-up 0.6s cubic-bezier(0.16,1,0.3,1) 0.3s forwards',
            }}
          >
            Master English, Medicine & AI — With the Power of{' '}
            <span className="text-burnt-orange">40 Years</span>
          </h1>

          {/* Subheadline */}
          <p
            className="text-body-large text-white/70 mb-10 max-w-2xl"
            style={{
              opacity: 0,
              animation: 'fade-in-up 0.5s cubic-bezier(0.16,1,0.3,1) 0.8s forwards',
            }}
          >
            Five revolutionary AI-powered platforms trusted by 10,000+ students
            across 60+ countries. From IELTS preparation to medical OSCE training
            — your future starts here.
          </p>

          {/* CTA Group */}
          <div
            className="flex flex-wrap gap-4 mb-12"
            style={{
              opacity: 0,
              animation: 'fade-in-up 0.4s cubic-bezier(0.16,1,0.3,1) 1.0s forwards',
            }}
          >
            <button onClick={() => scrollToSection('platforms')} className="btn-primary">
              Explore Our Platforms
            </button>
            <button onClick={() => scrollToSection('free-tools')} className="btn-secondary border-white text-white hover:bg-white hover:text-deep-green">
              Try Free Tools
            </button>
          </div>

          {/* Trust Row */}
          <div
            className="flex flex-wrap gap-x-8 gap-y-3"
            style={{
              opacity: 0,
              animation: 'fade-in-up 0.4s cubic-bezier(0.16,1,0.3,1) 1.2s forwards',
            }}
          >
            {[
              { icon: Calendar, text: '40+ Years' },
              { icon: Users, text: '10,000+ Students' },
              { icon: MapPin, text: '60+ Countries' },
              { icon: Award, text: 'British Council Accredited' },
            ].map(({ icon: Icon, text }) => (
              <div key={text} className="flex items-center gap-2 text-muted-olive">
                <Icon size={16} className="shrink-0" />
                <span className="font-body font-medium text-sm">{text}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Social proof floating cards */}
        <div className="hidden xl:block absolute right-12 top-1/2 -translate-y-1/2">
          {[
            { rotate: '-5deg', translate: '-20px', yOffset: '-80px', icon: Users, title: '10,000+', desc: 'Students taught since 1986', color: '#D4653B' },
            { rotate: '0deg', translate: '0px', yOffset: '0px', icon: Globe, title: '60+', desc: 'Countries worldwide', color: '#8BA888' },
            { rotate: '5deg', translate: '20px', yOffset: '80px', icon: Award, title: 'British Council', desc: 'Accredited since 1986', color: '#FDF6E3' },
          ].map((card, i) => {
            const IconComp = card.icon;
            return (
              <div
                key={i}
                className="w-56 rounded-xl bg-white/15 backdrop-blur-md border border-white/25 absolute animate-fade-in-up p-4 shadow-lg"
                style={{
                  transform: `rotate(${card.rotate}) translateX(${card.translate}) translateY(${card.yOffset})`,
                  animationDelay: `${1.4 + i * 0.2}s`,
                  animationDuration: '0.8s',
                }}
              >
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0" style={{ backgroundColor: `${card.color}30` }}>
                    <IconComp size={20} style={{ color: card.color }} />
                  </div>
                  <div>
                    <div className="text-white font-bold text-lg leading-tight">{card.title}</div>
                    <div className="text-white/60 text-xs leading-tight">{card.desc}</div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 2: Platform Showcase ─────────────────── */
const platforms = [
  {
    name: '12-Language AI Tutor',
    accent: '#8BA888',
    description:
      'Learn English, French, Spanish, German, Italian, Portuguese, Chinese, Arabic, Vietnamese, Indonesian, Korean & Japanese with your personal AI tutor.',
    features: ['AI-powered lessons', 'Native pronunciation', 'CEFR certification'],
    price: 'Free / £12.99/mo Premium',
    url: 'https://anglotec-ai.com/',
    image: '/platform-12-language.png',
  },
  {
    name: 'UKVI & OET Exam Prep',
    accent: '#D4653B',
    description:
      'AI voice speaking coach, writing evaluator, and adaptive practice for IELTS, UKVI IELTS & OET. Get instant band scores and personalized feedback.',
    features: ['AI speaking coach', 'Writing evaluator', 'Full mock tests'],
    price: 'Free tier available',
    url: 'https://agmp.anglotec.com/',
    image: '/platform-exam-prep.png',
  },
  {
    name: 'OSCE Training & NHS Careers',
    accent: '#2C4A3E',
    description:
      '805+ AI OSCE scenarios for PLAB 2. NHS CV review, mock interviews with AI feedback, and job placement support.',
    features: ['805+ OSCE scenarios', 'NHS CV review', 'AI mock interviews'],
    price: 'Free tier available',
    url: 'https://amcvdo.anglotec-ai.com/',
    image: '/platform-osce.png',
  },
  {
    name: 'Medical & Clinical AI Tutor',
    accent: '#C44D56',
    description:
      'AI patient cases, history taking practice, physical examination training, and clinical reasoning for medical professionals.',
    features: ['AI patient simulation', 'Clinical reasoning', 'Voice interactions'],
    price: 'Free / From £22.99/mo',
    url: 'https://amc.anglotec-ai.com/',
    image: '/platform-medical.png',
  },
  {
    name: 'AI Prompt Engineering Masterclass',
    accent: '#A68B6B',
    description:
      '9,000 AI prompts across 12 categories. Code generation, content creation, business strategy, and more. Level up your AI skills.',
    features: ['9,000+ prompts', '12 categories', 'XP tracking'],
    price: 'Free / From £14.99/mo',
    url: 'https://masterclass.anglotec-ai.com/',
    image: '/platform-masterclass.png',
  },
];

function PlatformCard({ platform, index }: { platform: typeof platforms[0]; index: number }) {
  const { ref, visible } = useScrollReveal(0.2);

  return (
    <div
      ref={ref}
      className="platform-card flex flex-col h-full group"
      style={{
        borderTop: `4px solid ${platform.accent}`,
        opacity: visible ? 1 : 0,
        transform: visible ? 'translateY(0)' : 'translateY(40px)',
        transition: `all 0.5s cubic-bezier(0.16, 1, 0.3, 1) ${index * 0.1}s`,
      }}
    >
      <div className="mb-4 overflow-hidden rounded-lg">
        <img
          src={platform.image}
          alt={platform.name}
          className="w-full h-40 object-cover group-hover:scale-105 transition-transform duration-500"
          loading="lazy"
        />
      </div>
      <h3 className="text-h4 font-body font-semibold text-text-primary mb-2">
        {platform.name}
      </h3>
      <p className="text-body-small text-text-secondary mb-4 flex-1">
        {platform.description}
      </p>
      <ul className="space-y-2 mb-4">
        {platform.features.map((f) => (
          <li key={f} className="flex items-center gap-2 text-body-small text-text-secondary">
            <CheckCircle size={14} className="text-sage-green shrink-0" />
            {f}
          </li>
        ))}
      </ul>
      <p className="font-mono text-xs text-muted-olive uppercase tracking-wider mb-4">
        {platform.price}
      </p>
      <a
        href={platform.url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-1 text-burnt-orange font-body font-medium text-sm hover:gap-2 transition-all duration-200"
      >
        Learn More <ArrowRight size={16} />
      </a>
    </div>
  );
}

function PlatformShowcase() {
  const { ref: headerRef, visible: headerVisible } = useScrollReveal(0.15);

  return (
    <section id="platforms" className="bg-off-white section-padding">
      <div className="container-main">
        {/* Header */}
        <div
          ref={headerRef}
          className="text-center mb-16"
          style={{
            opacity: headerVisible ? 1 : 0,
            transform: headerVisible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
          }}
        >
          <p className="text-caption text-muted-olive mb-3">Five Platforms</p>
          <h2 className="text-h2 font-heading text-deep-green mb-4">
            One Academy, Unlimited Possibilities
          </h2>
          <p className="text-body text-text-secondary max-w-2xl mx-auto">
            Each platform is powered by advanced AI, designed by British education
            experts, and trusted by professionals worldwide.
          </p>
        </div>

        {/* Cards Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
          {platforms.slice(0, 3).map((p, i) => (
            <PlatformCard key={p.name} platform={p} index={i} />
          ))}
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 lg:gap-8 mt-6 lg:mt-8 max-w-2xl mx-auto">
          {platforms.slice(3).map((p, i) => (
            <PlatformCard key={p.name} platform={p} index={i + 3} />
          ))}
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 3: Free Tools Banner ─────────────────── */
const tools = [
  {
    name: 'IELTS Calculator',
    description: 'Calculate your band score instantly with personalized study tips.',
    icon: Calculator,
    path: '/ielts-calculator',
  },
  {
    name: 'OET Speaking',
    description: 'Practice with realistic role-play cards for nurses and doctors.',
    icon: Mic,
    path: '/oet-speaking',
  },
  {
    name: 'OSCE Scenarios',
    description: 'Generate random medical OSCE stations with timers.',
    icon: Stethoscope,
    path: '/osce-practice',
  },
  {
    name: 'AI Prompts',
    description: 'Get optimized AI prompts for coding, writing & business.',
    icon: Sparkles,
    path: '/ai-prompt-generator',
  },
];

function FreeToolsBanner() {
  const { ref: headerRef, visible: headerVisible } = useScrollReveal(0.15);

  return (
    <section id="free-tools" className="gradient-warm py-16 md:py-20">
      <div className="container-main">
        <div
          ref={headerRef}
          className="text-center mb-12"
          style={{
            opacity: headerVisible ? 1 : 0,
            transform: headerVisible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
          }}
        >
          <p className="text-caption text-muted-olive mb-3">Free Resources</p>
          <h2 className="text-h2 font-heading text-deep-green mb-4">
            Tools That Go Viral. Knowledge That Sticks.
          </h2>
          <p className="text-body text-text-secondary max-w-xl mx-auto">
            Our free interactive tools are used by thousands of students every
            month. Try them now — no signup required.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-10">
          {tools.map((tool, i) => {
            const { ref, visible } = useScrollReveal(0.15);
            const Icon = tool.icon;
            return (
              <Link
                key={tool.name}
                to={tool.path}
                ref={ref}
                className="tool-card flex flex-col items-start"
                style={{
                  opacity: visible ? 1 : 0,
                  transform: visible ? 'translateY(0)' : 'translateY(30px)',
                  transition: `all 0.4s cubic-bezier(0.16, 1, 0.3, 1) ${i * 0.08}s`,
                }}
              >
                <div className="w-10 h-10 rounded-lg bg-burnt-orange/10 flex items-center justify-center mb-3">
                  <Icon size={20} className="text-burnt-orange" />
                </div>
                <h4 className="font-body font-semibold text-base text-text-primary mb-1">
                  {tool.name}
                </h4>
                <p className="text-body-small text-text-secondary">
                  {tool.description}
                </p>
              </Link>
            );
          })}
        </div>

        <div className="text-center">
          <Link to="/ielts-calculator" className="btn-secondary inline-flex">
            Explore All Free Tools <ArrowRight size={16} className="ml-2" />
          </Link>
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 4: Trust & Social Proof ─────────────────── */
const stats = [
  { value: 1986, suffix: '', label: 'Founded' },
  { value: 40, suffix: '+', label: 'Years of Excellence' },
  { value: 10000, suffix: '+', label: 'Students Taught' },
  { value: 60, suffix: '+', label: 'Countries Represented' },
];

const testimonials = [
  {
    quote:
      'The IELTS AI speaking coach helped me score Band 8.0. The feedback on my pronunciation was incredibly detailed.',
    name: 'Dr. Priya K.',
    role: 'India',
  },
  {
    quote:
      'I passed my PLAB 2 OSCE on the first attempt thanks to the 805+ scenarios. The AI feedback on my clinical communication was invaluable.',
    name: 'Dr. James O.',
    role: 'Nigeria',
  },
  {
    quote:
      'Learning English with AI tutor felt like having a personal teacher. My confidence improved dramatically in just 3 months.',
    name: 'Maria L.',
    role: 'Philippines',
  },
];

function TrustSection() {
  const { ref: statsRef, visible: statsVisible } = useScrollReveal(0.2);
  const { ref: testRef, visible: testVisible } = useScrollReveal(0.15);

  return (
    <section className="bg-off-white section-padding">
      <div className="container-main">
        {/* Stats Bar */}
        <div
          ref={statsRef}
          className="grid grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-4 mb-20 lg:mb-24"
        >
          {stats.map((stat, i) => (
            <div
              key={stat.label}
              className={`text-center relative ${
                i < stats.length - 1 ? 'lg:after:content-[""] lg:after:absolute lg:after:right-0 lg:after:top-1/2 lg:after:-translate-y-1/2 lg:after:w-px lg:after:h-12 lg:after:bg-warm-gray' : ''
              }`}
            >
              <div className="text-h1 font-heading text-deep-green mb-1">
                {statsVisible ? (
                  <CountUp
                    end={stat.value}
                    duration={2}
                    separator=","
                    suffix={stat.suffix}
                  />
                ) : (
                  `0${stat.suffix}`
                )}
              </div>
              <p className="text-body-small text-text-secondary">{stat.label}</p>
            </div>
          ))}
        </div>

        {/* Testimonials */}
        <div ref={testRef}>
          <div className="text-center mb-12">
            <p
              className="text-caption text-muted-olive mb-3"
              style={{
                opacity: testVisible ? 1 : 0,
                transform: testVisible ? 'translateY(0)' : 'translateY(20px)',
                transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
              }}
            >
              Student Success Stories
            </p>
            <h2
              className="text-h2 font-heading text-deep-green max-w-3xl mx-auto"
              style={{
                opacity: testVisible ? 1 : 0,
                transform: testVisible ? 'translateY(0)' : 'translateY(20px)',
                transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.1s',
              }}
            >
              Trusted by Medical Professionals & Language Learners Worldwide
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {testimonials.map((t, i) => (
              <div
                key={t.name}
                className="bg-white rounded-2xl p-6 shadow-card relative"
                style={{
                  opacity: testVisible ? 1 : 0,
                  transform: testVisible ? 'translateY(0)' : 'translateY(30px)',
                  transition: `all 0.5s cubic-bezier(0.16, 1, 0.3, 1) ${0.15 + i * 0.15}s`,
                }}
              >
                <Quote
                  size={32}
                  className="text-sage-green/20 absolute top-4 left-4"
                />
                <p className="text-body text-text-primary font-medium mb-6 relative z-10 pt-6">
                  &ldquo;{t.quote}&rdquo;
                </p>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-warm-gray flex items-center justify-center">
                    <span className="font-body font-semibold text-sm text-deep-green">
                      {t.name.charAt(0)}
                    </span>
                  </div>
                  <div>
                    <p className="font-body font-semibold text-sm text-text-primary">
                      {t.name}
                    </p>
                    <p className="text-body-small text-text-secondary">{t.role}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 5: Why Choose Anglotec ─────────────────── */
const reasons = [
  {
    icon: Shield,
    title: 'British Council Accredited',
    description:
      'Officially recognized by the British Council since 1986, ensuring the highest standards of educational quality.',
  },
  {
    icon: Brain,
    title: 'AI-Powered Personalization',
    description:
      'Every student gets a personalized learning path powered by advanced AI that adapts in real-time to your progress.',
  },
  {
    icon: GraduationCap,
    title: 'Expert-Led Content',
    description:
      'All courses are designed by British education experts and medical professionals with decades of experience.',
  },
  {
    icon: Globe,
    title: 'Global Community',
    description:
      'Join 10,000+ students from 60+ countries. Learn alongside doctors, nurses, and professionals worldwide.',
  },
  {
    icon: Gift,
    title: 'Free Tools & Resources',
    description:
      'Access our suite of free viral tools — IELTS calculators, OSCE generators, and AI prompt libraries.',
  },
  {
    icon: TrendingUp,
    title: 'Proven Results',
    description:
      'Our students consistently achieve top scores in IELTS, OET, and PLAB examinations.',
  },
];

function WhyChooseSection() {
  const { ref: headerRef, visible: headerVisible } = useScrollReveal(0.15);

  return (
    <section className="bg-deep-green text-white section-padding">
      <div className="container-main">
        <div
          ref={headerRef}
          className="text-center mb-16"
          style={{
            opacity: headerVisible ? 1 : 0,
            transform: headerVisible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
          }}
        >
          <p className="text-caption text-muted-olive mb-3">Why Anglotec</p>
          <h2 className="text-h2 font-heading text-white mb-4">
            British Quality. AI Innovation. Global Reach.
          </h2>
          <p className="text-body-large text-white/70 max-w-2xl mx-auto">
            For over four decades, we&apos;ve set the standard for English language
            education. Now, we&apos;re pioneering the future of AI-powered learning.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
          {reasons.map((r, i) => {
            const { ref, visible } = useScrollReveal(0.15);
            const Icon = r.icon;
            return (
              <div
                key={r.title}
                ref={ref}
                className="group"
                style={{
                  opacity: visible ? 1 : 0,
                  transform: visible ? 'translateY(0) scale(1)' : 'translateY(30px) scale(0.97)',
                  transition: `all 0.4s cubic-bezier(0.16, 1, 0.3, 1) ${i * 0.08}s`,
                }}
              >
                <div className="w-10 h-10 rounded-lg bg-burnt-orange/20 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                  <Icon size={20} className="text-burnt-orange" />
                </div>
                <h4 className="font-body font-semibold text-h4 text-white mb-2">
                  {r.title}
                </h4>
                <p className="text-body-small text-white/70">{r.description}</p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 5b: Our Scarborough Campus ─────────────────── */
function CampusSection() {
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setVisible(true); },
      { threshold: 0.15 }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  const photos = [
    { src: '/campus-entrance.jpg', alt: 'Anglotec Academy entrance in Scarborough' },
    { src: '/campus-students.jpg', alt: 'Students and staff at Anglotec Academy' },
    { src: '/campus-conservatory.jpg', alt: 'The historic conservatory at Anglotec' },
  ];

  return (
    <section className="bg-off-white py-20 md:py-28" ref={ref}>
      <div className="container-main">
        <div
          className={`text-center mb-14 transition-all duration-700 ${visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'}`}
        >
          <p className="text-caption text-burnt-orange mb-3">Our Campus</p>
          <h2 className="text-section-title font-heading text-deep-green mb-4">
            Study in a 19th Century English Manor House
          </h2>
          <p className="text-body-large text-warm-gray max-w-2xl mx-auto">
            Our physical campus in Scarborough, England — British Council accredited since 1986,
            welcoming students from 60+ countries.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {photos.map((photo, i) => (
            <div
              key={i}
              className={`rounded-xl overflow-hidden shadow-md group transition-all duration-700 ${visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}
              style={{ transitionDelay: `${i * 150}ms` }}
            >
              <div className="overflow-hidden">
                <img
                  src={photo.src}
                  alt={photo.alt}
                  className="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500"
                />
              </div>
            </div>
          ))}
        </div>

        <div
          className={`mt-10 flex flex-wrap justify-center gap-6 transition-all duration-700 delay-500 ${visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}
        >
          <div className="flex items-center gap-2 text-warm-gray">
            <MapPin size={18} className="text-burnt-orange" />
            <span className="text-sm">20 Avenue Road, Scarborough, YO12 5JX, UK</span>
          </div>
          <div className="flex items-center gap-2 text-warm-gray">
            <Award size={18} className="text-sage-green" />
            <span className="text-sm">British Council Accredited Since 1986</span>
          </div>
          <div className="flex items-center gap-2 text-warm-gray">
            <Globe size={18} className="text-burnt-orange" />
            <span className="text-sm">60+ Nationalities</span>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ─────────────────── Section 6: Pricing Comparison ─────────────────── */
const pricingPlans = [
  {
    name: 'Free Forever',
    price: '0',
    period: '',
    features: [
      '12-Language AI Tutor (1 language)',
      'IELTS Calculator',
      'OET Speaking Practice',
      'OSCE Scenario Generator',
      'AI Prompt Generator (100 prompts)',
      'Language Guide',
    ],
    cta: 'Get Started',
    highlighted: false,
  },
  {
    name: 'Premium',
    badge: 'MOST POPULAR',
    price: '£12.99',
    period: '/mo',
    features: [
      'All 12 languages + 6 GCSE courses',
      'AI Speaking Coach',
      'AI Writing Evaluator',
      '805+ OSCE Scenarios',
      '9,000 AI Prompts',
      'NHS CV Review',
      'Priority Support',
    ],
    cta: 'Start Premium',
    highlighted: true,
  },
  {
    name: 'Residency',
    price: '£59.99',
    period: '/mo',
    features: [
      'Everything in Premium',
      'Unlimited AI Patients',
      'Complete Medical Tutor',
      'Residency Exam Prep',
      '1-on-1 Expert Sessions',
      'Team Features',
    ],
    cta: 'Go Residency',
    highlighted: false,
  },
];

function PricingSection() {
  const { ref: headerRef, visible: headerVisible } = useScrollReveal(0.15);

  return (
    <section className="bg-off-white section-padding">
      <div className="container-main">
        <div
          ref={headerRef}
          className="text-center mb-16"
          style={{
            opacity: headerVisible ? 1 : 0,
            transform: headerVisible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
          }}
        >
          <p className="text-caption text-muted-olive mb-3">Simple Pricing</p>
          <h2 className="text-h2 font-heading text-deep-green mb-4">
            Start Free. Upgrade When You&apos;re Ready.
          </h2>
          <p className="text-body text-text-secondary max-w-xl mx-auto">
            Every platform offers a generous free tier. No credit card required
            to start learning.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-5xl mx-auto items-start">
          {pricingPlans.map((plan, i) => {
            const { ref, visible } = useScrollReveal(0.15);
            return (
              <div
                key={plan.name}
                ref={ref}
                className={`rounded-2xl p-6 lg:p-8 transition-all duration-500 ${
                  plan.highlighted
                    ? 'bg-white border-2 border-burnt-orange shadow-premium scale-[1.02] md:scale-105'
                    : 'bg-white border border-warm-gray shadow-card'
                }`}
                style={{
                  opacity: visible ? 1 : 0,
                  transform: visible
                    ? plan.highlighted
                      ? 'translateY(0) scale(1.02)'
                      : 'translateY(0)'
                    : 'translateY(40px)',
                  transition: `all 0.5s cubic-bezier(0.16, 1, 0.3, 1) ${i * 0.12}s`,
                }}
              >
                {plan.badge && (
                  <span className="inline-block bg-burnt-orange text-white font-mono text-[10px] uppercase tracking-wider px-3 py-1 rounded-full mb-4">
                    {plan.badge}
                  </span>
                )}
                <h3 className="font-body font-semibold text-xl text-text-primary mb-2">
                  {plan.name}
                </h3>
                <div className="flex items-baseline gap-1 mb-6">
                  <span className="text-h1 font-heading text-deep-green">
                    {plan.price}
                  </span>
                  {plan.period && (
                    <span className="text-body text-text-secondary">{plan.period}</span>
                  )}
                </div>
                <ul className="space-y-3 mb-8">
                  {plan.features.map((f, fi) => (
                    <li
                      key={f}
                      className="flex items-start gap-2 text-body-small text-text-secondary"
                      style={{
                        opacity: visible ? 1 : 0,
                        transition: `opacity 0.3s ease ${fi * 0.03}s`,
                      }}
                    >
                      <CheckCircle size={16} className="text-sage-green shrink-0 mt-0.5" />
                      {f}
                    </li>
                  ))}
                </ul>
                <button
                  className={`w-full py-3 px-6 rounded-lg font-body font-semibold text-sm uppercase tracking-wider transition-all duration-200 ${
                    plan.highlighted
                      ? 'bg-burnt-orange text-white hover:scale-[1.03] hover:shadow-cta'
                      : 'border-2 border-deep-green text-deep-green hover:bg-deep-green hover:text-white'
                  }`}
                >
                  {plan.cta}
                </button>
              </div>
            );
          })}
        </div>

        <p className="text-center text-caption text-text-secondary mt-10">
          All plans include a 14-day free trial. Cancel anytime.
        </p>
      </div>
    </section>
  );
}

/* ─────────────────── Section 7: Final CTA ─────────────────── */
function FinalCTA() {
  const { ref, visible } = useScrollReveal(0.15);
  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section ref={ref} className="gradient-hero section-padding relative overflow-hidden">
      <div
        className="absolute inset-0 opacity-[0.06]"
        style={{ backgroundImage: 'url(/hero-bg-pattern.svg)', backgroundSize: 'cover' }}
      />
      <ParticleField />

      <div className="container-main relative z-10 text-center">
        <h2
          className="text-h1 font-heading text-white mb-6"
          style={{
            opacity: visible ? 1 : 0,
            transform: visible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)',
          }}
        >
          Start Your Learning Journey Today
        </h2>
        <p
          className="text-body-large text-white/70 max-w-2xl mx-auto mb-10"
          style={{
            opacity: visible ? 1 : 0,
            transform: visible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.1s',
          }}
        >
          Join 10,000+ students from 60+ countries who trust Anglotec AI Academy.
        </p>
        <div
          className="flex flex-wrap justify-center gap-4 mb-12"
          style={{
            opacity: visible ? 1 : 0,
            transform: visible ? 'translateY(0)' : 'translateY(30px)',
            transition: 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.2s',
          }}
        >
          <button onClick={() => scrollToSection('platforms')} className="btn-primary">
            Explore Platforms
          </button>
          <button
            onClick={() => scrollToSection('free-tools')}
            className="inline-flex items-center justify-center px-8 py-3 border-2 border-white text-white bg-transparent font-body font-semibold text-sm uppercase tracking-wider rounded-lg transition-all duration-200 hover:bg-white hover:text-deep-green"
          >
            Try Free Tools
          </button>
        </div>
        <p
          className="font-mono text-xs text-muted-olive tracking-wider"
          style={{
            opacity: visible ? 1 : 0,
            transition: 'opacity 0.6s ease 0.4s',
          }}
        >
          British Council Accredited Since 1986 &middot; English UK Member
        </p>
      </div>
    </section>
  );
}

/* ─────────────────── Home Page ─────────────────── */
export default function Home() {
  return (
    <Layout>
      <HeroSection />
      <PlatformShowcase />
      <FreeToolsBanner />
      <TrustSection />
      <WhyChooseSection />
      <CampusSection />
      <PricingSection />
      <FinalCTA />
    </Layout>
  );
}
