import React from 'react';

const Footer = () => {
  return (
    <div className='sticky bottom-0 flex w-full min-h-24 shadow-[0px_0px_4px_rgba(0,0,0,0.3)] font-Source-Sans'>
      <div className='mx-auto p-2'>
        <p className='text-slate-50 text-sm font-bold'>NFL Livescore Bot - {(new Date().getFullYear())}</p>
      </div>
    </div>
  )
}

export default Footer;
