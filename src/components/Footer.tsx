import { Link } from 'react-router';
import { Globe, Mail, Phone, MapPin } from 'lucide-react';

const platformLinks = [
  { name: '12-Language AI Tutor', url: 'https://anglotec-ai.com/' },
  { name: 'UKVI & OET Exam Prep', url: 'https://agmp.anglotec.com/' },
  { name: 'OSCE Training & NHS', url: 'https://amcvdo.anglotec-ai.com/' },
  { name: 'Medical AI Tutor', url: 'https://amc.anglotec-ai.com/' },
  { name: 'AI Prompt Masterclass', url: 'https://masterclass.anglotec-ai.com/' },
];

const toolLinks = [
  { name: 'IELTS Calculator', path: '/ielts-calculator' },
  { name: 'OET Speaking Practice', path: '/oet-speaking' },
  { name: 'OSCE Practice', path: '/osce-practice' },
  { name: 'AI Prompt Generator', path: '/ai-prompt-generator' },
  { name: 'Language Guide', path: '/language-guide' },
];

export default function Footer() {
  return (
    <footer className="bg-deep-green text-white">
      <div className="container-main py-16 md:py-20">
        {/* Main Footer Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-12">
          {/* About Column */}
          <div className="sm:col-span-2 lg:col-span-1">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center">
                <span className="text-white font-heading font-bold text-sm">A</span>
              </div>
              <div className="flex flex-col">
                <span className="font-heading font-bold text-lg leading-tight">Anglotec</span>
                <span className="font-mono text-[9px] uppercase tracking-widest text-muted-olive">
                  AI Academy
                </span>
              </div>
            </div>
            <p className="text-white/70 text-body-small leading-relaxed mb-4">
              British Council accredited since 1986. Pioneering AI-powered education
              for English language, medical training, and professional development.
            </p>
            <div className="flex items-center gap-2 text-muted-olive">
              <img src="/trust-seal-1986.svg" alt="Est. 1986" className="w-10 h-10" />
              <img src="/british-council-logo.svg" alt="British Council" className="h-8" />
            </div>
          </div>

          {/* Platforms Column */}
          <div>
            <h4 className="font-body font-semibold text-sm uppercase tracking-wider mb-4">
              Platforms
            </h4>
            <ul className="space-y-3">
              {platformLinks.map((link) => (
                <li key={link.url}>
                  <a
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-white/70 text-body-small hover:text-burnt-orange transition-colors duration-200 hover:translate-x-1 inline-block"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Free Tools Column */}
          <div>
            <h4 className="font-body font-semibold text-sm uppercase tracking-wider mb-4">
              Free Tools
            </h4>
            <ul className="space-y-3">
              {toolLinks.map((link) => (
                <li key={link.path}>
                  <Link
                    to={link.path}
                    className="text-white/70 text-body-small hover:text-burnt-orange transition-colors duration-200 hover:translate-x-1 inline-block"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact Column */}
          <div>
            <h4 className="font-body font-semibold text-sm uppercase tracking-wider mb-4">
              Contact
            </h4>
            <ul className="space-y-3">
              <li className="flex items-center gap-2 text-white/70 text-body-small">
                <Mail size={16} className="text-burnt-orange shrink-0" />
                <span>info@anglotec.com</span>
              </li>
              <li className="flex items-center gap-2 text-white/70 text-body-small">
                <Phone size={16} className="text-burnt-orange shrink-0" />
                <span>+44(0)1723 367141</span>
              </li>
              <li className="flex items-start gap-2 text-white/70 text-body-small">
                <MapPin size={16} className="text-burnt-orange shrink-0 mt-0.5" />
                <span>20 Avenue Road, Scarborough, YO12 5JX, England</span>
              </li>
              <li className="flex items-center gap-2 text-white/70 text-body-small">
                <Globe size={16} className="text-burnt-orange shrink-0" />
                <a href="https://new.anglotec.com" target="_blank" rel="noopener noreferrer" className="hover:text-burnt-orange transition-colors">new.anglotec.com</a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-12 pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="font-mono text-xs text-muted-olive">
            &copy; {new Date().getFullYear()} Anglotec AI Academy. All rights reserved.
          </p>
          <p className="font-mono text-xs text-muted-olive">
            British Council Accredited Since 1986 &middot; English UK Member
          </p>
        </div>
      </div>
    </footer>
  );
}
